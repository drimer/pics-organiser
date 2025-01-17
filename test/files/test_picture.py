import os
import pytest

from files.picture import Picture, InvalidFileType


TEST_ASSETS_ABS_PATH = os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir, 'test_assets')


def test_that_picture_fails_to_load_non_picture_file():
    with pytest.raises(InvalidFileType):
        Picture(os.path.join(TEST_ASSETS_ABS_PATH, "text1.txt"))
