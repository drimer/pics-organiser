from datetime import datetime

import mock

from tasks.reports import (
    PictureReporterByMissingExifDate,
)


def test_picture_matcher_by_missing_exif_date():
    mock_picture = mock.Mock()
    mock_picture.datetime_taken = None

    matcher = PictureReporterByMissingExifDate()
    assert matcher.should_report(mock_picture) is True


def test_picture_matcher_by_missing_exif_date_does_not_match():
    mock_picture = mock.Mock()
    mock_picture.datetime_taken = datetime(2023, 10, 1)

    matcher = PictureReporterByMissingExifDate()
    assert matcher.should_report(mock_picture) is False
