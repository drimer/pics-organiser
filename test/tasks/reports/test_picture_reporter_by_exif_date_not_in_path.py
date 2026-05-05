from datetime import datetime
import os

import mock

from tasks.reports import (
    PictureReporterByExifDateNotInPath,
)


def test_picture_matcher_by_exif_date_not_in_path_mathes():
    mock_picture = mock.Mock()
    mock_picture.datetime_taken = datetime(2023, 10, 1)
    mock_picture.dirname = "/path/to/pics/2024/10. Oct/01. great day"
    mock_picture.path = os.path.join(mock_picture.dirname, "pic.jpg")

    matcher = PictureReporterByExifDateNotInPath()
    assert matcher.should_report(mock_picture) is True


def test_picture_matcher_by_exif_date_not_in_path_year_does_not_match():
    mock_picture = mock.Mock()
    mock_picture.datetime_taken = datetime(2023, 10, 1)
    mock_picture.dirname = "/path/to/pics/2024/10. Oct/01. great day"
    mock_picture.path = os.path.join(mock_picture.dirname, "pic.jpg")

    matcher = PictureReporterByExifDateNotInPath()
    assert matcher.should_report(mock_picture) is True


def test_picture_matcher_by_exif_date_not_in_path_month_does_not_match():
    mock_picture = mock.Mock()
    mock_picture.datetime_taken = datetime(2023, 10, 1)
    mock_picture.dirname = "/path/to/pics/2023/11. Nov/01. great day"
    mock_picture.path = os.path.join(mock_picture.dirname, "pic.jpg")

    matcher = PictureReporterByExifDateNotInPath()
    assert matcher.should_report(mock_picture) is True


def test_picture_matcher_by_exif_date_not_in_path_allow_end_of_year_to_carry_over():
    mock_picture = mock.Mock()
    mock_picture.datetime_taken = datetime(2024, 1, 1)
    mock_picture.dirname = "/path/to/pics/2023/12. Dec/01. great day"
    mock_picture.path = os.path.join(mock_picture.dirname, "pic.jpg")

    matcher = PictureReporterByExifDateNotInPath()
    assert matcher.should_report(mock_picture) is False


def test_picture_matcher_by_exif_date_not_in_path_allow_first_of_year_in_its_folder():
    mock_picture = mock.Mock()
    mock_picture.datetime_taken = datetime(2024, 1, 1)
    mock_picture.dirname = "/path/to/pics/2024/1. Jan/01. great day"
    mock_picture.path = os.path.join(mock_picture.dirname, "pic.jpg")

    matcher = PictureReporterByExifDateNotInPath()
    assert matcher.should_report(mock_picture) is False


def test_picture_matcher_by_exif_date_not_in_path_incorrect_month_folder_matches():
    mock_picture = mock.Mock()
    mock_picture.datetime_taken = datetime(2023, 10, 2)
    mock_picture.dirname = "/path/to/pics/2023/11. Nov/01. great day"
    mock_picture.path = os.path.join(mock_picture.dirname, "pict.jpg")

    matcher = PictureReporterByExifDateNotInPath()
    assert matcher.should_report(mock_picture) is True


def test_picture_matcher_by_exif_date_not_in_path_ignores_year_in_filename():
    mock_picture = mock.Mock()
    mock_picture.datetime_taken = datetime(2023, 10, 2)
    mock_picture.dirname = "/path/to/pics/2024/10. Oct"
    mock_picture.path = os.path.join(mock_picture.dirname, "IMG-20231002-WA0000.jpg")

    matcher = PictureReporterByExifDateNotInPath()
    assert matcher.should_report(mock_picture) is True


def test_picture_matcher_by_exif_date_not_in_path_ignores_month_in_filename():
    mock_picture = mock.Mock()
    mock_picture.datetime_taken = datetime(2023, 10, 2)
    mock_picture.dirname = "/path/to/pics/2023/11. Nov"
    mock_picture.path = os.path.join(mock_picture.dirname, "IMG-20231102-WA0000.jpg")

    matcher = PictureReporterByExifDateNotInPath()
    assert matcher.should_report(mock_picture) is True
