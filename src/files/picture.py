import datetime
import os
import shutil
from collections import defaultdict

from PIL import Image
import piexif


class InvalidFileType(Exception):
    pass


def is_image_file(path):
    return path.lower().endswith(('.png', '.jpg', '.jpeg'))


def copy_file(src_path, dest_path):
    target_dirname = os.path.dirname(dest_path)
    if not os.path.exists(target_dirname):
        os.makedirs(target_dirname)

    shutil.copy(src_path, dest_path)


class Picture(object):
    '''Picture file in disk'''

    def __init__(self, path):
        if not is_image_file(path):
            raise InvalidFileType('File %s is not a piture' % path)

        self.path = path
        self.__metadata = {}

    def __repr__(self):
        return self.path

    @property
    def filename(self):
        return os.path.basename(self.path)

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


class PicturesCollection(object):

    def __init__(self, path):
        self.pictures = []
        self.add_from_folder(path)

    def add_from_folder(self, path):
        '''Searches for pictures in path recursively'''
        picture_finder = PictureFinder(path)
        for picture in picture_finder.find_all():
            self.pictures.append(picture)

    def sort_into_folder(self, path):
        '''Copies all pictures in collection to specified folder'''
        sorted_collection = SortedPicturesCollection(path)
        for picture in self.pictures:
            if picture.datetime_taken is None:
                dest_dir = 'unknown/'
            else:
                year = picture.datetime_taken.year
                month = picture.datetime_taken.month
                day = picture.datetime_taken.day
                dest_dir = '%04d/%02d/%02d/' % (year, month, day)
            sorted_collection.add(dest_dir, picture)

        sorted_collection.save_to_disk()


class SortedPicturesCollection(object):
    def __init__(self, root_dir):
        self.root_dir = root_dir
        self.__all_directories = []
        self.__pictures_in_dirs = defaultdict(list)

    def add(self, directory, picture):
        if directory not in self.__all_directories:
            self.__all_directories.append(directory)
            self.__all_directories.sort()
        self.__pictures_in_dirs[directory].append(picture)

    def save_to_disk(self):
        last_pic_number_used = 1
        for directory in self.__all_directories:
            for picture in self.__pictures_in_dirs[directory]:
                dest_path = os.path.join(
                    self.root_dir,
                    directory,
                    '%05d.jpg' % last_pic_number_used
                )
                copy_file(picture.path, dest_path)
                last_pic_number_used += 1


class PictureFinder(object):

    def __init__(self, path):
        assert os.path.isdir(path)

        self.path = path

    def find_all(self):
        for root, _, files in os.walk(self.path):
            for filename in files:
                abs_path = os.path.join(root, filename)
                if is_image_file(abs_path):
                    yield Picture(abs_path)
