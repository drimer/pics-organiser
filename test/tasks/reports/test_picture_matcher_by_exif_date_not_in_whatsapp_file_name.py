from datetime import datetime

import mock

from tasks.reports import (
    PictureReporterByExifDateNotInWhatsappFileName,
)


def test_picture_matcher_by_exif_date_not_in_whatsapp_file_name_matches():
    mock_picture = mock.Mock()
    mock_picture.datetime_taken = datetime(2023, 10, 1)
    mock_picture.filename = "IMG-20231001-WA0000.jpg"

    matcher = PictureReporterByExifDateNotInWhatsappFileName()
    assert matcher.should_report(mock_picture) is False


def test_picture_matcher_by_exif_date_not_in_whatsapp_file_name_does_not_match():
    mock_picture = mock.Mock()
    mock_picture.datetime_taken = datetime(2023, 10, 1)
    mock_picture.filename = "IMG-20231001-WA0000.jpg"

    matcher = PictureReporterByExifDateNotInWhatsappFileName()
    assert matcher.should_report(mock_picture) is False


def test_picture_matcher_by_exif_date_not_in_whatsapp_file_name_does_not_match_seven_days_in_past():
    mock_picture = mock.Mock()
    mock_picture.datetime_taken = datetime(2023, 10, 25)
    mock_picture.filename = "IMG-20231101-WA0000.jpg"

    matcher = PictureReporterByExifDateNotInWhatsappFileName()
    assert matcher.should_report(mock_picture) is False


def test_picture_matcher_by_exif_date_not_in_whatsapp_file_name_matches_eight_days_in_past():
    mock_picture = mock.Mock()
    mock_picture.datetime_taken = datetime(2023, 10, 24)
    mock_picture.filename = "IMG-20231101-WA0000.jpg"

    matcher = PictureReporterByExifDateNotInWhatsappFileName()
    assert matcher.should_report(mock_picture) is True
