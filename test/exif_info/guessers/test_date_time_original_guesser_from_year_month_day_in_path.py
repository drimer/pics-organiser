import time
from unittest import mock

from exif_info.guessers import DateTimeOriginalGuesserFromYearMonthDayInPath


def test_happy_path():
    assert (
        DateTimeOriginalGuesserFromYearMonthDayInPath().get(
            mock.Mock(path="2023/10. October/1. Vienna trip/IMG_1234.jpg")
        )
        == "2023:10:01"
    )


def test_that_cannot_guess_when_no_day():
    assert (
        DateTimeOriginalGuesserFromYearMonthDayInPath().get(
            mock.Mock(path="2023/10. October/IMG_1234.jpg")
        )
        is None
    )


def test_that_cannot_guess_when_no_month():
    assert (
        DateTimeOriginalGuesserFromYearMonthDayInPath().get(
            mock.Mock(path="2023/1. Vienna trip/IMG_1234.jpg")
        )
        is None
    )


def test_that_cannot_guess_when_day_looks_like_day_but_over_31():
    assert (
        DateTimeOriginalGuesserFromYearMonthDayInPath().get(
            mock.Mock(path="2023/10. October/32. Vienna trip/IMG_1234.jpg")
        )
        is None
    )


def test_that_cannot_guess_when_year_looks_like_year_but_in_the_future():
    year_in_future = time.localtime().tm_year + 1
    assert (
        DateTimeOriginalGuesserFromYearMonthDayInPath().get(
            mock.Mock(path=f"{year_in_future}/10. October/1. Vienna trip/IMG_1234.jpg")
        )
        is None
    )


def test_that_cannot_guess_when_month_looks_like_month_but_over_12():
    assert (
        DateTimeOriginalGuesserFromYearMonthDayInPath().get(
            mock.Mock(path="2023/13. December/1. Vienna trip/IMG_1234.jpg")
        )
        is None
    )


def test_that_cannot_guess_with_no_indication():
    assert (
        DateTimeOriginalGuesserFromYearMonthDayInPath().get(
            mock.Mock(path="family pics/cousins/IMG_1234.jpg")
        )
        is None
    )
