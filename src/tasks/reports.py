import abc
from datetime import datetime
from typing import Generator, Iterable

from files.manager import PictureManager
from files.picture import Picture


class PictureReporter(abc.ABC):

    @abc.abstractmethod
    def should_report(self, picture: Picture) -> bool:
        pass

    @property
    @abc.abstractmethod
    def description(self) -> str:
        pass


class PictureReporterByExifDateNotInPath(PictureReporter):
    def should_report(self, picture: Picture) -> bool:
        if picture.datetime_taken is None:
            return False

        if picture.datetime_taken.month == 1 and picture.datetime_taken.day == 1:
            # Allow end of year to carry over to the next year
            if (
                str(picture.datetime_taken.year - 1) in picture.dirname
                and "12" in picture.dirname
            ):
                return False

        return (
            str(picture.datetime_taken.year) not in picture.dirname
            or str(picture.datetime_taken.month) not in picture.dirname
        )

    @property
    def description(self) -> str:
        return "EXIF date not in the path"


class PictureReporterByExifDateNotInWhatsappFileName(PictureReporter):
    NUMBER_OF_DAYS_WHATSAPP_FILE_NAME_CAN_BE_OFF = 7

    def should_report(self, picture: Picture) -> bool:
        if picture.datetime_taken is None:
            return False

        example_length = len("IMG-20220101-WA0000.jpg")
        if len(picture.filename) != example_length:
            return False

        if not picture.filename.startswith("IMG-") or "-WA" not in picture.filename:
            return False

        # Allow a time window for WhatsApp file names, as people sometimes forget to share the picture immediately,
        # and the file name is generated when the picture is shared.
        filename_date = datetime.strptime(picture.filename[4:12], "%Y%m%d")
        date_difference = abs((picture.datetime_taken - filename_date).days)
        if date_difference <= self.NUMBER_OF_DAYS_WHATSAPP_FILE_NAME_CAN_BE_OFF:
            return False

        start_filename = f"IMG-{picture.datetime_taken.year}{picture.datetime_taken.month:02d}{picture.datetime_taken.day:02d}"  # noqa: E501
        return not picture.filename.startswith(start_filename)

    @property
    def description(self) -> str:
        return "EXIF date does not match the whatsapp file name"


class PictureReporterByMissingExifDate(PictureReporter):
    def should_report(self, picture: Picture) -> bool:
        return picture.datetime_taken is None

    @property
    def description(self) -> str:
        return "Missing EXIF date"


class PictureReporterByMissingExifLocation(PictureReporter):
    def should_report(self, picture: Picture) -> bool:
        if picture.location is None:
            return True
        elif picture.location.alt == (1, 1) and picture.location.alt_ref == 0:
            # I ran the script to set EXIF GPS with these values, but they aren't picked up
            # by Android's Photo app. So I need these included in the report.
            return True

        return False

    @property
    def description(self) -> str:
        return "Missing EXIF location"


def find_and_report_imgs(
    path: str, reporters: Iterable[PictureReporter], picture_manager: PictureManager
) -> Generator[tuple[Picture, PictureReporter], None, None]:
    for picture in picture_manager.find_images(path):
        for reporter in reporters:
            if reporter.should_report(picture):
                yield picture, reporter
