import abc
from typing import Generator, List

from files.manager import PictureManager
from files.picture import Picture


class PictureMatcher(abc.ABC):

    @abc.abstractmethod
    def apply(self, picture: Picture) -> bool:
        pass


class PictureMatcherByWrongDateInExif(PictureMatcher):
    def apply(self, picture: Picture) -> bool:
        if picture.datetime_taken is None:
            return False

        return (
            str(picture.datetime_taken.year) not in picture.path
            or str(picture.datetime_taken.month) not in picture.path
            or str(picture.datetime_taken.day) not in picture.path
        )


class PictureMatcherByMissingExifDate(PictureMatcher):
    def apply(self, picture: Picture) -> bool:
        return picture.datetime_taken is None


def find_and_report_imgs(
    path: str, filter: PictureMatcher, picture_manager: PictureManager
) -> Generator[Picture, None, None]:
    for picture in picture_manager.find_images(path):
        if filter.apply(picture):
            yield picture


def report_imgs_without_exif_date(
    path: str, picture_manager: PictureManager
) -> Generator[Picture, None, None]:
    return find_and_report_imgs(
        path, PictureMatcherByMissingExifDate(), picture_manager
    )


def report_imgs_without_exif_location(
    path: str, picture_manager: PictureManager
) -> Generator[Picture, None, None]:
    pictures_collection = picture_manager.find_images(path)
    for picture in pictures_collection:
        if picture.location is None:
            yield picture


def report_imgs_where_exif_date_not_in_path(
    path: str, picture_manager: PictureManager
) -> List[Picture]:
    images_without_date = []

    for picture in picture_manager.find_images(path):
        possible_year = next(
            (
                part
                for part in picture.parent_folders_as_list
                if part.isdigit() and len(part) == 4
            ),
            None,
        )
        possible_month = next(
            (
                part
                for part in picture.parent_folders_as_list
                if part.isdigit() and len(part) in (1, 2)
            ),
            None,
        )
        if not possible_month:
            for part in picture.parent_folders_as_list:
                try:
                    possible_month = part.split(".")[0]
                except:
                    pass

        if possible_year and possible_month:
            if picture.datetime_taken is None:
                images_without_date.append(picture)
            elif str(picture.datetime_taken.year) != possible_year:
                images_without_date.append(picture)
            elif str(picture.datetime_taken.month) != possible_month:
                images_without_date.append(picture)

    return images_without_date
