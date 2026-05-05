from datetime import datetime
import os

import mock

from tasks.reports import (
    PictureReporterByExifDateNotInPath,
)


def test_that_is_reported_when_exif_date_not_in_path():
    mock_picture = mock.Mock()
    mock_picture.datetime_taken = datetime(2023, 10, 1)
    mock_picture.dirname = "/path/to/pics/2024/10. Oct/01. great day"
    mock_picture.path = os.path.join(mock_picture.dirname, "pic.jpg")

    matcher = PictureReporterByExifDateNotInPath()
    assert matcher.should_report(mock_picture) is True


def test_that_is_reported_when_year_does_not_match():
    mock_picture = mock.Mock()
    mock_picture.datetime_taken = datetime(2023, 10, 1)
    mock_picture.dirname = "/path/to/pics/2024/10. Oct/01. great day"
    mock_picture.path = os.path.join(mock_picture.dirname, "pic.jpg")

    matcher = PictureReporterByExifDateNotInPath()
    assert matcher.should_report(mock_picture) is True


def test_that_is_reported_when_month_does_not_match():
    mock_picture = mock.Mock()
    mock_picture.datetime_taken = datetime(2023, 10, 1)
    mock_picture.dirname = "/path/to/pics/2023/11. Nov/01. great day"
    mock_picture.path = os.path.join(mock_picture.dirname, "pic.jpg")

    matcher = PictureReporterByExifDateNotInPath()
    assert matcher.should_report(mock_picture) is True


def test_that_allows_end_of_year_to_carry_over():
    mock_picture = mock.Mock()
    mock_picture.datetime_taken = datetime(2024, 1, 1)
    mock_picture.dirname = "/path/to/pics/2023/12. Dec/01. great day"
    mock_picture.path = os.path.join(mock_picture.dirname, "pic.jpg")

    matcher = PictureReporterByExifDateNotInPath()
    assert matcher.should_report(mock_picture) is False


def test_that_allows_first_of_year_in_its_folder():
    mock_picture = mock.Mock()
    mock_picture.datetime_taken = datetime(2024, 1, 1)
    mock_picture.dirname = "/path/to/pics/2024/1. Jan/01. great day"
    mock_picture.path = os.path.join(mock_picture.dirname, "pic.jpg")

    matcher = PictureReporterByExifDateNotInPath()
    assert matcher.should_report(mock_picture) is False


def test_that_is_reported_when_month_in_folder_does_not_match():
    mock_picture = mock.Mock()
    mock_picture.datetime_taken = datetime(2023, 10, 2)
    mock_picture.dirname = "/path/to/pics/2023/11. Nov/01. great day"
    mock_picture.path = os.path.join(mock_picture.dirname, "pict.jpg")

    matcher = PictureReporterByExifDateNotInPath()
    assert matcher.should_report(mock_picture) is True


def test_that_is_reported_when_year_in_filename_does_not_match():
    mock_picture = mock.Mock()
    mock_picture.datetime_taken = datetime(2023, 10, 2)
    mock_picture.dirname = "/path/to/pics/2024/10. Oct"
    mock_picture.path = os.path.join(mock_picture.dirname, "IMG-20231002-WA0000.jpg")

    matcher = PictureReporterByExifDateNotInPath()
    assert matcher.should_report(mock_picture) is True


def test_that_is_reported_when_month_in_filename_does_not_match():

    mock_picture = mock.Mock()
    mock_picture.datetime_taken = datetime(2023, 10, 2)
    mock_picture.dirname = "/path/to/pics/2023/11. Nov"
    mock_picture.path = os.path.join(mock_picture.dirname, "IMG-20231102-WA0000.jpg")

    matcher = PictureReporterByExifDateNotInPath()
    assert matcher.should_report(mock_picture) is True
