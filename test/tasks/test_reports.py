from datetime import datetime

import mock

from tasks.reports import (
    PictureMatcherByExifDateNotInPath,
    PictureMatcherByMissingExifDate,
    PictureMatcherByMissingExifLocation,
    find_and_report_imgs,
)


def test_find_and_report_imgs_with_a_match():
    mock_picture = mock.Mock()
    mock_picture.datetime_taken = datetime(2023, 10, 1)

    mock_picture_manager = mock.Mock()
    mock_picture_manager.find_images.return_value = [mock_picture]

    matcher = mock.Mock()
    matcher.apply.return_value = True

    result = list(find_and_report_imgs("dummy_path", matcher, mock_picture_manager))

    assert len(result) == 1
    assert result[0] == mock_picture


def test_find_and_report_imgs_without_a_match():
    mock_picture = mock.Mock()
    mock_picture.datetime_taken = datetime(2023, 10, 1)

    mock_picture_manager = mock.Mock()
    mock_picture_manager.find_images.return_value = [mock_picture]

    matcher = mock.Mock()
    matcher.apply.return_value = False

    result = list(find_and_report_imgs("dummy_path", matcher, mock_picture_manager))

    assert len(result) == 0


def test_picture_matcher_by_exif_date_not_in_path_mathes():
    mock_picture = mock.Mock()
    mock_picture.datetime_taken = datetime(2023, 10, 1)
    mock_picture.path = "/path/to/pics/2023/10. Oct/01. great day/pic.jpg"

    matcher = PictureMatcherByExifDateNotInPath()
    assert matcher.apply(mock_picture) is False


def test_picture_matcher_by_exif_date_not_in_path_year_does_not_match():
    mock_picture = mock.Mock()
    mock_picture.datetime_taken = datetime(2023, 10, 1)
    mock_picture.path = "/path/to/pics/2024/10. Oct/01. great day/pic.jpg"

    matcher = PictureMatcherByExifDateNotInPath()
    assert matcher.apply(mock_picture) is True


def test_picture_matcher_by_exif_date_not_in_path_month_does_not_match():
    mock_picture = mock.Mock()
    mock_picture.datetime_taken = datetime(2023, 10, 1)
    mock_picture.path = "/path/to/pics/2023/11. Nov/01. great day/pic.jpg"

    matcher = PictureMatcherByExifDateNotInPath()
    assert matcher.apply(mock_picture) is True


def test_picture_matcher_by_missing_exif_date():
    mock_picture = mock.Mock()
    mock_picture.datetime_taken = None

    matcher = PictureMatcherByMissingExifDate()
    assert matcher.apply(mock_picture) is True


def test_picture_matcher_by_missing_exif_date_does_not_match():
    mock_picture = mock.Mock()
    mock_picture.datetime_taken = datetime(2023, 10, 1)

    matcher = PictureMatcherByMissingExifDate()
    assert matcher.apply(mock_picture) is False


def test_picture_matcher_by_missing_exif_location_matches():
    mock_picture = mock.Mock()
    mock_picture.location = None

    matcher = PictureMatcherByMissingExifLocation()
    assert matcher.apply(mock_picture) is True


def test_picture_matcher_by_missing_exif_location_does_not_match():
    mock_picture = mock.Mock()
    mock_picture.location = (10.0, 20.0)

    matcher = PictureMatcherByMissingExifLocation()
    assert matcher.apply(mock_picture) is False
