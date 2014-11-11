from nose.tools import assert_in, raises

from src.picture import (
    InvalidFileType,
    Picture,
    PictureFinder,
)


@raises(InvalidFileType)
def test_txt_is_not_picture():
    Picture('test/files/text1.txt')


def test_jpg_is_picture():
    Picture('test/files/DSC00470.JPG')


def test_dsc00316_has_exif_data():
    pic = Picture('test/files/DSC00316.JPG')
    assert len(pic.exif_metadata)


def test_picture_finder_finds_jpg_pics():
    finder = PictureFinder('test/files')
    pics_found = [pic.path for pic in finder.find_all()]
    assert_in('test/files/DSC00316.JPG', pics_found)
    assert_in('test/files/DSC00325.JPG', pics_found)
    assert_in('test/files/DSC00470.JPG', pics_found)
    assert_in('test/files/DSC01051.JPG', pics_found)
    assert_in('test/files/DSC02228.JPG', pics_found)
    assert_in('test/files/more/DSC02228.JPG', pics_found)


def test_picture_finder_does_not_find_txts():
    finder = PictureFinder('test/files')
    pics_found = list(finder.find_all())
    assert 'test/files/text1.txt' not in pics_found
