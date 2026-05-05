import time

import mock

from exif_info.guessers import DatetimeOriginalGuesserFromYearMonthInPath


def test_happy_path():
    assert (
        DatetimeOriginalGuesserFromYearMonthInPath().get(
            mock.Mock(path="2023/10. October/IMG_1234.jpg")
        )
        == "2023:10:15"
    )


def test_that_cannot_guess_when_no_year_month():
    assert (
        DatetimeOriginalGuesserFromYearMonthInPath().get(
            mock.Mock(path="family pics/cousins/IMG_1234.jpg")
        )
        is None
    )


def test_that_cannot_guess_when_path_looks_like_month_but_over_12():
    assert (
        DatetimeOriginalGuesserFromYearMonthInPath().get(
            mock.Mock(path="2023/13. December/IMG_1234.jpg")
        )
        is None
    )


def test_that_cannot_guess_when_year_looks_like_year_but_in_the_future():
    year_in_future = time.localtime().tm_year + 1
    assert (
        DatetimeOriginalGuesserFromYearMonthInPath().get(
            mock.Mock(path=f"{year_in_future}/10. October/IMG_1234.jpg")
        )
        is None
    )
