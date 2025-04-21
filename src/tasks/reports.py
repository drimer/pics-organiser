import abc
from typing import Generator

from files.manager import PictureManager
from files.picture import Picture


class PictureMatcher(abc.ABC):

    @abc.abstractmethod
    def apply(self, picture: Picture) -> bool:
        pass


class PictureMatcherByExifDateNotInPath(PictureMatcher):
    def apply(self, picture: Picture) -> bool:
        if picture.datetime_taken is None:
            return False

        return (
            str(picture.datetime_taken.year) not in picture.path
            or str(picture.datetime_taken.month) not in picture.path
        )


class PictureMatcherByMissingExifDate(PictureMatcher):
    def apply(self, picture: Picture) -> bool:
        return picture.datetime_taken is None


class PictureMatcherByMissingExifLocation(PictureMatcher):
    def apply(self, picture: Picture) -> bool:
        return picture.location is None


def find_and_report_imgs(
    path: str, matcher: PictureMatcher, picture_manager: PictureManager
) -> Generator[Picture, None, None]:
    for picture in picture_manager.find_images(path):
        if matcher.apply(picture):
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
    return find_and_report_imgs(
        path, PictureMatcherByMissingExifLocation(), picture_manager
    )
