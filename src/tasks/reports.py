import abc
from datetime import datetime
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

        if picture.datetime_taken.month == 1 and picture.datetime_taken.day == 1:
            # Allow end of year to carry over to the next year
            if (
                str(picture.datetime_taken.year - 1) in picture.path
                and "12" in picture.path
            ):
                return False

        return (
            str(picture.datetime_taken.year) not in picture.path
            or str(picture.datetime_taken.month) not in picture.path
        )
        

class PictureMatcherByExifDateNotInWhatsappFileName(PictureMatcher):
    NUMBER_OF_DAYS_WHATSAPP_FILE_NAME_CAN_BE_OFF = 5
    
    def apply(self, picture: Picture) -> bool:
        if picture.datetime_taken is None:
            return False
        
        example_length = len("IMG-20220101-WA0000.jpg")
        if len(picture.filename) != example_length or not picture.filename.startswith("IMG-") or '-WA' not in picture.filename:
            return False
        
        # Allow a time window for WhatsApp file names, as people sometimes forget to share the picture immediately,
        # and the file name is generated when the picture is shared.
        filename_date = datetime.strptime(picture.filename[4:12], "%Y%m%d")
        date_difference = abs((picture.datetime_taken - filename_date).days)
        if date_difference <= self.NUMBER_OF_DAYS_WHATSAPP_FILE_NAME_CAN_BE_OFF:
            return False
        
        start_filename = f"IMG-{picture.datetime_taken.year}{picture.datetime_taken.month:02d}{picture.datetime_taken.day:02d}"
        return not picture.filename.startswith(start_filename)


class PictureMatcherByMissingExifDate(PictureMatcher):
    def apply(self, picture: Picture) -> bool:
        return picture.datetime_taken is None


class PictureMatcherByMissingExifLocation(PictureMatcher):
    def apply(self, picture: Picture) -> bool:
        if picture.location is None:
            return True
        elif picture.location.alt == (1, 1) and picture.location.alt_ref == 0:
            # I ran the script to set EXIF GPS with these values, but they aren't picked up
            # by Android's Photo app. So I need these included in the report.
            return True

        return False


def find_and_report_imgs(
    path: str, matchers: tuple[PictureMatcher, ...], picture_manager: PictureManager
) -> Generator[Picture, None, None]:
    for picture in picture_manager.find_images(path):
        if any(matcher.apply(picture) for matcher in matchers):
            yield picture


def report_imgs_without_exif_date(
    path: str, picture_manager: PictureManager
) -> Generator[Picture, None, None]:
    return find_and_report_imgs(
        path, (PictureMatcherByMissingExifDate(),), picture_manager
    )


def report_imgs_without_exif_location(
    path: str, picture_manager: PictureManager
) -> Generator[Picture, None, None]:
    return find_and_report_imgs(
        path, (PictureMatcherByMissingExifLocation(),), picture_manager
    )
