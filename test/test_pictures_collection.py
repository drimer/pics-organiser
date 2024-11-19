import os
import shutil

from files.picture import InvalidFileType, Picture
from files.collections import PicturesCollection


def assert_file_is_picture(path):
    assert os.path.exists(path), '%s does not exist' % path
    try:
        Picture(path)
    except InvalidFileType:
        raise AssertionError('%s is not a picture' % path)


class TestPicturesCollection(object):
    def setUp(self):
        self.sorted_pics_dir = 'test_assets_sorted'
        if os.path.exists(self.sorted_pics_dir):
            shutil.rmtree(self.sorted_pics_dir)
        os.mkdir(self.sorted_pics_dir)

    def tearDown(self):
        shutil.rmtree(self.sorted_pics_dir)

    def test_pictures_collection_is_sorted(self):
        collection = PicturesCollection('test_assets')
        collection.sort_into_folder('test_assets_sorted')
        sorted_pics_paths = (
            'test_assets_sorted/2010/09/15/00001.jpg',
            'test_assets_sorted/2010/09/15/00002.jpg',
            'test_assets_sorted/2010/09/20/00003.jpg',
            'test_assets_sorted/2011/02/09/00004.jpg',
            'test_assets_sorted/2011/07/18/00005.jpg',
            'test_assets_sorted/2011/07/18/00006.jpg',
        )
        for pic_path in sorted_pics_paths:
            assert_file_is_picture(pic_path)
