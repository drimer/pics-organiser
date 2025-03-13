import os

import pytest

from files.picture import InvalidFileType, Picture, get_path_as_list

TEST_ASSETS_ABS_PATH = os.path.join(
    os.path.dirname(__file__), os.path.pardir, os.path.pardir, "test_assets"
)


def test_that_picture_fails_to_load_non_picture_file():
    with pytest.raises(InvalidFileType):
        Picture(os.path.join(TEST_ASSETS_ABS_PATH, "text1.txt"))


def test_that_get_path_as_list_returns_full_list():
    expected_path_list = ["users", "foo", "fotos", "2025", "1. Jan", "me.jpg"]

    assert get_path_as_list(os.path.join(*expected_path_list)) == expected_path_list


def test_that_location_is_none_if_no_gps():
    picture = Picture(os.path.join(TEST_ASSETS_ABS_PATH, "pexels-zoorg.jpg"))

    assert picture.location is None


def test_that_location_is_identified_when_it_is_set():
    picture = Picture(os.path.join(TEST_ASSETS_ABS_PATH, "loaded_chips.jpg"))

    assert picture.location is not None
