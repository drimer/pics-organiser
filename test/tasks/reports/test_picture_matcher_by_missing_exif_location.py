import mock

from files.picture import ExifGpsLocation
from tasks.reports import (
    PictureReporterByMissingExifLocation,
)


def test_picture_matcher_by_missing_exif_location_matches():
    mock_picture = mock.Mock()
    mock_picture.location = None

    matcher = PictureReporterByMissingExifLocation()
    assert matcher.should_report(mock_picture) is True


def test_picture_matcher_by_missing_exif_location_does_not_match():
    mock_picture = mock.Mock()
    mock_picture.location = ExifGpsLocation(
        lat=12.345, lat_ref="N", lon=6.789, lon_ref="W", alt=0, alt_ref=(0, 0)
    )

    matcher = PictureReporterByMissingExifLocation()
    assert matcher.should_report(mock_picture) is False


def test_picture_matcher_by_missing_exif_location_matches_broken_data():
    mock_picture = mock.Mock()
    mock_picture.location = ExifGpsLocation(
        lat=12.345, lat_ref="N", lon=6.789, lon_ref="W", alt=(1, 1), alt_ref=0
    )

    matcher = PictureReporterByMissingExifLocation()
    assert matcher.should_report(mock_picture) is True
