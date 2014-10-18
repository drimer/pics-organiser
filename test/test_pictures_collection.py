import os
import shutil

from src.picture import InvalidFileType, Picture, PicturesCollection


def assert_file_is_picture(path):
    assert os.path.exists(path), '%s does not exist' % path
    try:
        Picture(path)
    except InvalidFileType:
        raise AssertionError('%s is not a picture' % path)


class TestPicturesCollection(object):
    def setup(self):
        self.sorted_pics_dir = 'test/sorted_pictures'
        if os.path.exists(self.sorted_pics_dir):
            shutil.rmtree(self.sorted_pics_dir)
        os.mkdir(self.sorted_pics_dir)

    def teardown(self):
        shutil.rmtree(self.sorted_pics_dir)

    def test_pictures_collection_is_sorted(self):
        collection = PicturesCollection('test/files')
        collection.sort_into_folder('test/sorted_pictures')
        sorted_pics_paths = (
            'test/sorted_pictures/2010/09/15/DSC00316.JPG',
            'test/sorted_pictures/2010/09/15/DSC00325.JPG',
            'test/sorted_pictures/2010/09/20/DSC00470.JPG',
            'test/sorted_pictures/2011/02/09/DSC01051.JPG',
            'test/sorted_pictures/2011/07/18/DSC02228.JPG',
        )
        for pic_path in sorted_pics_paths:
            assert_file_is_picture(pic_path)
