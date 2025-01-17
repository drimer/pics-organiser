import os

import pytest

from files.picture import (
    InvalidFileType,
    Picture,
)
from files.manager import PictureManager

TEST_ASSETS_ABS_PATH = os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir, 'test_assets')


def test_find_images_finds_only_pics():
    finder = PictureManager()
    pics_found = list(finder.find_images(TEST_ASSETS_ABS_PATH))

    assert Picture(os.path.join(TEST_ASSETS_ABS_PATH, 'DSC00316.JPG')) in pics_found
    assert Picture(os.path.join(TEST_ASSETS_ABS_PATH, 'DSC00325.JPG')) in pics_found
    assert Picture(os.path.join(TEST_ASSETS_ABS_PATH, 'DSC00470.JPG')) in pics_found
    assert Picture(os.path.join(TEST_ASSETS_ABS_PATH, 'DSC01051.JPG')) in pics_found
    assert Picture(os.path.join(TEST_ASSETS_ABS_PATH, 'DSC02228.JPG')) in pics_found
    assert Picture(os.path.join(TEST_ASSETS_ABS_PATH, 'more', 'DSC0001.JPG')) in pics_found
    assert Picture(os.path.join(TEST_ASSETS_ABS_PATH, 'more', 'DSC02228.JPG')) in pics_found
