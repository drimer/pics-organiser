from collections import defaultdict
import os
import shutil
from files.file import File
from files.manager import PictureFinder


class FilesCollection:
    def __init__(self, files=[]):
        self.files = files
        
    def __iter__(self):
        return iter(self.files)

    def add_file(self, file: File):
        self.files.append(file)

    def get_files(self):
        return self.files


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
                

def copy_file(src_path, dest_path):
    target_dirname = os.path.dirname(dest_path)
    if not os.path.exists(target_dirname):
        os.makedirs(target_dirname)

    shutil.copy(src_path, dest_path)

