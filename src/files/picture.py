import datetime
from collections import defaultdict

from PIL import Image
import piexif

from files.file import File


def is_image_file(path):
    return path.lower().endswith(('.png', '.jpg', '.jpeg'))


class InvalidFileType(Exception):
    pass


class Picture(File):
    """Picture file in disk"""

    def __init__(self, path):
        if not is_image_file(path):
            raise InvalidFileType('File %s is not a picture' % path)

        super().__init__(path)
        self.__metadata = {}

    @property
    def exif_metadata(self):
        img = Image.open(self.path)
        
        if 'exif' in img.info:
            try:
                self.__metadata = piexif.load(img.info['exif'])
            except:
                self.__metadata = defaultdict(dict)
        else:
            self.__metadata = defaultdict(dict)

        return self.__metadata

    @property
    def datetime_taken(self):
        bin_datetime = self.exif_metadata['Exif'].get(piexif.ExifIFD.DateTimeOriginal)
        if bin_datetime:
            return datetime.datetime.strptime(bin_datetime.decode(), '%Y:%m:%d %H:%M:%S')
    
    @datetime_taken.setter
    def datetime_taken(self, value):
        self.exif_metadata['Exif'][piexif.ExifIFD.DateTimeOriginal] = value
