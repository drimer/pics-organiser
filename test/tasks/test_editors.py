import mock

from exif_info.guessers import ExifInfoGuesser


def test_guess_date_bin_from_full_path_happy_path_for_year_month_day():
    assert (
        ExifInfoGuesser().get_date_time_original(
            mock.Mock(path="2023/10. October/1. Vienna trip/IMG_1234.jpg")
        )
        == b"2023:10:01 12:34:56"
    )


def test_guess_date_bin_from_full_path_happy_path_for_year_month():
    assert (
        ExifInfoGuesser().get_date_time_original(
            mock.Mock(path="2023/10. October/IMG_1234.jpg")
        )
        == b"2023:10:15 12:34:56"
    )


def test_guess_date_bin_from_full_path_happy_path_for_whatsapp_file():
    assert (
        ExifInfoGuesser().get_date_time_original(
            mock.Mock(path="family pics/cousins/IMG-20130803-WA0006.jpg")
        )
        == b"2013:08:03 12:34:56"
    )


def test_guess_date_bin_from_full_path_happy_path_for_whatsapp_file_in_year_month_day():
    assert (
        ExifInfoGuesser().get_date_time_original(
            mock.Mock(path="2023/10. October/1. Vienna trip/IMG-20231001-WA0006.jpg")
        )
        == b"2023:10:01 12:34:56"
    )


def test_guess_date_bin_from_full_path_no_date_in_path():
    assert (
        ExifInfoGuesser().get_date_time_original(
            mock.Mock(path="family pics/cousins/IMG_1234.jpg")
        )
        is None
    )
