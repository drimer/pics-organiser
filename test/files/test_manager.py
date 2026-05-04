import os

from files.manager import PictureManager
from files.picture import Picture

TEST_ASSETS_ABS_PATH = os.path.join(
    os.path.dirname(__file__), os.path.pardir, os.path.pardir, "test_assets"
)


def test_find_images_finds_only_pics():
    finder = PictureManager()
    pics_found = list(finder.find_images(TEST_ASSETS_ABS_PATH))

    expected_picuture_paths = (
        os.path.join(TEST_ASSETS_ABS_PATH, "DSC00316.JPG"),
        os.path.join(TEST_ASSETS_ABS_PATH, "DSC00325.JPG"),
        os.path.join(TEST_ASSETS_ABS_PATH, "DSC00470.JPG"),
        os.path.join(TEST_ASSETS_ABS_PATH, "DSC01051.JPG"),
        os.path.join(TEST_ASSETS_ABS_PATH, "DSC02228.JPG"),
        os.path.join(TEST_ASSETS_ABS_PATH, "IMG-20161121-WA0001.jpg"),
        os.path.join(TEST_ASSETS_ABS_PATH, "loaded_chips.jpg"),
        os.path.join(TEST_ASSETS_ABS_PATH, "pexels-zoorg.jpg"),
        os.path.join(TEST_ASSETS_ABS_PATH, "more", "DSC0001.JPG"),
        os.path.join(TEST_ASSETS_ABS_PATH, "more", "DSC02228.JPG"),
        os.path.join(
            TEST_ASSETS_ABS_PATH,
            "2020",
            "5. May",
            "4. birthday",
            "IMG-20161121-WA0001.jpg",
        ),
        os.path.join(
            TEST_ASSETS_ABS_PATH,
            "2020",
            "5. May",
            "4. birthday",
            "IMG-20210920-WA0001.jpg",
        ),
    )
    assert len(pics_found) == len(expected_picuture_paths)

    for expected_picuture_path in expected_picuture_paths:
        assert Picture(expected_picuture_path) in pics_found
