import time
from typing import Optional


from files.picture import Picture, get_path_as_list


class DateTimeOriginalGuesserFromWhatsappFile:
    def get(self, picture: Picture) -> Optional[bytes]:
        path_as_list = get_path_as_list(picture.path)
        sample_filename = "IMG-20130803-WA0006.jpg"

        try:
            filename = path_as_list[-1]
            if (
                not filename.startswith("IMG-")
                or "-WA" not in filename
                or len(filename) != len(sample_filename)
            ):
                return None

            date_str = filename[4:12]
            return f"{date_str[:4]}:{date_str[4:6]}:{date_str[6:]}"
        except (ValueError, IndexError):
            return None


class DateTimeOriginalGuesserFromYearMonthDayInPath:
    def get(self, picture: Picture) -> Optional[bytes]:
        path_as_list = get_path_as_list(picture.path)

        try:
            day_dir_name = path_as_list[-2]
            month_dir_name = path_as_list[-3]
            year_dir_name = path_as_list[-4]

            month_first_chars = month_dir_name.split(".")[0]
            month_str = f"{int(month_first_chars):0>2}"

            day_first_chars_possible_range = day_dir_name.split(".")[0]
            if "-" in day_first_chars_possible_range:
                day_first_chars = day_first_chars_possible_range.split("-")[0]
            else:
                day_first_chars = day_first_chars_possible_range
            day_str = f"{int(day_first_chars):0>2}"

            if (
                int(year_dir_name) > time.localtime().tm_year
                or int(month_str) > 12
                or int(day_str) > 31
            ):
                return None

            return f"{year_dir_name}:{month_str}:{day_str}"
        except (ValueError, IndexError):
            return None


class DatetimeOriginalGuesserFromYearMonthInPath:
    def get(self, picture: Picture) -> Optional[bytes]:
        path_as_list = get_path_as_list(picture.path)

        try:
            month_dir_name = path_as_list[-2]
            year_dir_name = path_as_list[-3]

            month_first_chars = month_dir_name.split(".")[0]
            month_str = f"{int(month_first_chars):0>2}"

            if int(year_dir_name) > time.localtime().tm_year or int(month_str) > 12:
                return None

            return f"{year_dir_name}:{month_str}:15"
        except (ValueError, IndexError):
            return None


class ExifInfoGuesser:
    # These are ordered from highest precedence to lowest.
    DATE_TIME_ORIGINAL_GUESSERS = (
        DateTimeOriginalGuesserFromWhatsappFile(),
        DateTimeOriginalGuesserFromYearMonthDayInPath(),
        DatetimeOriginalGuesserFromYearMonthInPath(),
    )

    def get_date_time_original(self, picture: Picture) -> Optional[bytes]:
        for guesser in self.DATE_TIME_ORIGINAL_GUESSERS:
            guess_attempt = guesser.get(picture)
            if guess_attempt:
                return f"{guess_attempt} 12:34:56".encode("ascii")

        return None
