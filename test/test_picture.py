import os

import pytest

from src.picture import (
    InvalidFileType,
    Picture,
    PictureFinder,
)

def test_txt_is_not_picture():
    with pytest.raises(InvalidFileType):
        Picture(os.path.join('test', 'files', 'text1.txt'))


def test_jpg_is_picture():
    Picture(os.path.join('test', 'files', 'DSC00470.JPG'))


def test_dsc00316_has_exif_data():
    pic = Picture(os.path.join('test', 'files', 'DSC00316.JPG'))
    assert len(pic.exif_metadata)


def test_picture_finder_finds_jpg_pics():
    finder = PictureFinder(os.path.join('test', 'files'))
    pics_found = [pic.path for pic in finder.find_all()]
    assert os.path.join('test', 'files', 'DSC00316.JPG') in pics_found
    assert os.path.join('test', 'files', 'DSC00325.JPG') in pics_found
    assert os.path.join('test', 'files', 'DSC00470.JPG') in pics_found
    assert os.path.join('test', 'files', 'DSC01051.JPG') in pics_found
    assert os.path.join('test', 'files', 'DSC02228.JPG') in pics_found
    assert os.path.join('test', 'files', 'more', 'DSC02228.JPG') in pics_found


def test_picture_finder_does_not_find_txts():
    finder = PictureFinder(os.path.join('test', 'files'))
    pics_found = list(finder.find_all())
    assert os.path.join('test', 'files', 'text1.txt') not in pics_found
