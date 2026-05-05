from datetime import datetime

import mock

from tasks.reports import (
    PictureReporterByMissingExifDate,
)


def test_that_is_reported_when_exif_date_is_missing():
    mock_picture = mock.Mock()
    mock_picture.datetime_taken = None

    matcher = PictureReporterByMissingExifDate()
    assert matcher.should_report(mock_picture) is True


def test_that_is_not_reported_when_exif_date_is_present():
    mock_picture = mock.Mock()
    mock_picture.datetime_taken = datetime(2023, 10, 1)

    matcher = PictureReporterByMissingExifDate()
    assert matcher.should_report(mock_picture) is False
