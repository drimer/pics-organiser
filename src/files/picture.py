import datetime
import os.path
from collections import defaultdict

import piexif
from PIL import Image

from files.file import File


def is_image_file(path):
    return path.lower().endswith((".png", ".jpg", ".jpeg"))


def get_path_as_list(path: str) -> list:
    return path.split(os.path.sep)


class InvalidFileType(Exception):
    pass


class Picture(File):
    """Picture file in disk"""

    def __init__(self, path):
        if not is_image_file(path):
            raise InvalidFileType("File %s is not a picture" % path)

        super().__init__(path)

        self.__metadata = defaultdict(dict)
        img = Image.open(self.path)
        if "exif" in img.info:
            try:
                self.__metadata = piexif.load(img.info["exif"])
            except:
                pass

    @property
    def exif_metadata(self):
        return self.__metadata

    @property
    def datetime_taken(self):
        bin_datetime = self.exif_metadata["Exif"].get(piexif.ExifIFD.DateTimeOriginal)
        if bin_datetime:
            return datetime.datetime.strptime(
                bin_datetime.decode(), "%Y:%m:%d %H:%M:%S"
            )

    @datetime_taken.setter
    def datetime_taken(self, value):
        self.exif_metadata["Exif"][piexif.ExifIFD.DateTimeOriginal] = value

    @property
    def location(self):
        gps = self.exif_metadata["GPS"]
        if not gps:
            return None

        lat = gps.get(piexif.GPSIFD.GPSLatitude)
        lon = gps.get(piexif.GPSIFD.GPSLongitude)
        if not lat or not lon:
            return None

        lat_ref = gps.get(piexif.GPSIFD.GPSLatitudeRef)
        lon_ref = gps.get(piexif.GPSIFD.GPSLongitudeRef)
        if not lat_ref or not lon_ref:
            return None

        return lat, lat_ref, lon, lon_ref
