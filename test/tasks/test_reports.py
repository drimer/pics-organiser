from datetime import datetime

import mock

from tasks.reports import (
    report_imgs_where_path_date_not_in_exif,
    report_imgs_without_exif_date,
)


def test_report_imgs_without_exif_date_nothing_found():
    pictureManagerMock = mock.MagicMock()
    pictureManagerMock.find_images.return_value = []

    result = report_imgs_without_exif_date("./test/files", pictureManagerMock)

    assert list(result) == []


def test_report_imgs_without_exif_date_one_image_found():
    pictureManagerMock = mock.MagicMock()
    pictureManagerMock.find_images.return_value = [
        mock.MagicMock(datetime_taken=None, path="test1.jpg"),
        mock.MagicMock(datetime_taken=datetime(2024, 4, 4, 14, 50), path="test2.jpg"),
    ]

    result = report_imgs_without_exif_date("./test/files", pictureManagerMock)

    assert list(result) == [pictureManagerMock.find_images.return_value[0]]


def test_report_imgs_without_exif_date_no_matches():
    pictureManagerMock = mock.MagicMock()
    pictureManagerMock.find_images.return_value = [
        mock.MagicMock(datetime_taken=datetime(2024, 4, 8, 14, 50), path="test1.jpg"),
        mock.MagicMock(datetime_taken=datetime(2024, 4, 4, 14, 50), path="test2.jpg"),
    ]

    result = report_imgs_without_exif_date("./test/files", pictureManagerMock)

    assert list(result) == []


def test_report_imgs_where_path_date_not_in_exif_nothing_found():
    pictureManagerMock = mock.MagicMock()
    pictureManagerMock.find_images.return_value = []

    result = report_imgs_where_path_date_not_in_exif("./test/files", pictureManagerMock)

    assert list(result) == []


def test_report_imgs_where_path_date_not_in_exif_found_one_without_date():
    pictureManagerMock = mock.MagicMock()
    pictureManagerMock.find_images.return_value = [
        mock.MagicMock(
            datetime_taken=None,
            path="C:/imgs/2024/10/07/test1.jpg",
            parent_folders_as_list=["C:", "imgs", "2024", "10", "07"],
        ),
        mock.MagicMock(
            datetime_taken=None,
            path="test2.jpg",
            parent_folders_as_list=["test2"],
        ),
    ]

    result = report_imgs_where_path_date_not_in_exif("./test/files", pictureManagerMock)

    assert list(result) == [pictureManagerMock.find_images.return_value[0]]


def test_report_imgs_where_path_date_not_in_exif_found_one_with_missing_only_day():
    pictureManagerMock = mock.MagicMock()
    pictureManagerMock.find_images.return_value = [
        mock.MagicMock(
            datetime_taken=datetime(2024, 10, 7, 14, 50),
            path="C:/imgs/2024/10/07/test1.jpg",
            parent_folders_as_list=["C:", "imgs", "2024", "10", "07"],
        ),
        mock.MagicMock(
            datetime_taken=None,
            path="C:/imgs/2024/06/test2.jpg",
            parent_folders_as_list=["C:", "imgs", "2024", "06"],
        ),
    ]

    result = report_imgs_where_path_date_not_in_exif("./test/files", pictureManagerMock)

    assert list(result) == [pictureManagerMock.find_images.return_value[1]]


def test_report_imgs_where_path_date_not_in_exif_found_one_with_missing_day_and_month_name():
    pictureManagerMock = mock.MagicMock()
    pictureManagerMock.find_images.return_value = [
        mock.MagicMock(
            datetime_taken=datetime(2024, 10, 7, 14, 50),
            path="C:/imgs/2024/10/07/test1.jpg",
            parent_folders_as_list=["C:", "imgs", "2024", "10", "07"],
        ),
        mock.MagicMock(
            datetime_taken=None,
            path="C:/imgs/2024/6. June/test2.jpg",
            parent_folders_as_list=["C:", "imgs", "2024", "6. June"],
        ),
    ]

    result = report_imgs_where_path_date_not_in_exif("./test/files", pictureManagerMock)

    assert list(result) == [pictureManagerMock.find_images.return_value[1]]


def test_report_imgs_where_path_date_and_exif_are_different():
    pictureManagerMock = mock.MagicMock()
    pictureManagerMock.find_images.return_value = [
        mock.MagicMock(
            datetime_taken=datetime(2024, 10, 7, 14, 50),
            path="C:/imgs/2024/10/07/test1.jpg",
            parent_folders_as_list=["C:", "imgs", "2024", "10", "07"],
        ),
        mock.MagicMock(
            datetime_taken=datetime(2024, 6, 7, 14, 50),
            path="C:/imgs/2023/6. June/test2.jpg",
            parent_folders_as_list=["C:", "imgs", "2023", "6. June"],
        ),
        mock.MagicMock(
            datetime_taken=datetime(2024, 6, 7, 14, 50),
            path="C:/imgs/2024/5. May/test2.jpg",
            parent_folders_as_list=["C:", "imgs", "2024", "5. May"],
        ),
    ]

    result = report_imgs_where_path_date_not_in_exif("./test/files", pictureManagerMock)

    assert list(result) == [
        pictureManagerMock.find_images.return_value[1],
        pictureManagerMock.find_images.return_value[2],
    ]
