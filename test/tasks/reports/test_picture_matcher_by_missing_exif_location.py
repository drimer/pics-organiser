import mock

from files.picture import ExifGpsLocation
from tasks.reports import (
    PictureReporterByMissingExifLocation,
)


def test_that_is_reported_when_exif_location_is_missing():
    mock_picture = mock.Mock()
    mock_picture.location = None

    matcher = PictureReporterByMissingExifLocation()
    assert matcher.should_report(mock_picture) is True


def test_that_is_not_reported_when_exif_location_is_present():
    mock_picture = mock.Mock()
    mock_picture.location = ExifGpsLocation(
        lat=12.345, lat_ref="N", lon=6.789, lon_ref="W", alt=0, alt_ref=(0, 0)
    )

    matcher = PictureReporterByMissingExifLocation()
    assert matcher.should_report(mock_picture) is False


def test_that_is_reported_when_exif_location_has_broken_data():
    mock_picture = mock.Mock()
    mock_picture.location = ExifGpsLocation(
        lat=12.345, lat_ref="N", lon=6.789, lon_ref="W", alt=(1, 1), alt_ref=0
    )

    matcher = PictureReporterByMissingExifLocation()
    assert matcher.should_report(mock_picture) is True
