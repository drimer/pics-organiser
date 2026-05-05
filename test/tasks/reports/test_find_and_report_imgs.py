from datetime import datetime

import mock

from tasks.reports import (
    find_and_report_imgs,
)


def test_find_and_report_imgs_with_a_match():
    mock_picture = mock.Mock()
    mock_picture.datetime_taken = datetime(2023, 10, 1)

    mock_picture_manager = mock.Mock()
    mock_picture_manager.find_images.return_value = [mock_picture]

    reporter_positive = mock.Mock()
    reporter_positive.should_report.return_value = True

    result = list(
        find_and_report_imgs("dummy_path", (reporter_positive,), mock_picture_manager)
    )

    assert len(result) == 1
    assert result[0] == (mock_picture, reporter_positive)


def test_find_and_report_imgs_without_a_match():
    mock_picture = mock.Mock()
    mock_picture.datetime_taken = datetime(2023, 10, 1)

    mock_picture_manager = mock.Mock()
    mock_picture_manager.find_images.return_value = [mock_picture]

    reporter_negative = mock.Mock()
    reporter_negative.should_report.return_value = False

    result = list(
        find_and_report_imgs("dummy_path", (reporter_negative,), mock_picture_manager)
    )

    assert len(result) == 0
