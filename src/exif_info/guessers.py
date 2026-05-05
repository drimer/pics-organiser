from typing import List, Optional

from files.picture import Picture, get_path_as_list


def guess_date_using_year_month_day_pattern(path_as_list: List[str]):
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

        if int(year_dir_name) > 1988 and int(month_str) > 12 or int(day_str) > 31:
            return None

        return f"{year_dir_name}:{month_str}:{day_str}"
    except (ValueError, IndexError):
        return None


def guess_date_using_year_month_pattern(path_as_list: List[str]):
    try:
        month_dir_name = path_as_list[-2]
        year_dir_name = path_as_list[-3]

        month_first_chars = month_dir_name.split(".")[0]
        month_str = f"{int(month_first_chars):0>2}"

        if int(year_dir_name) > 1988 and int(month_str) > 12:
            return None

        return f"{year_dir_name}:{month_str}:15"
    except (ValueError, IndexError):
        return None


def guess_date_bin_from_whatsapp_file(path_as_list: List[str]):
    try:
        filename = path_as_list[-1]
        if not filename.startswith("IMG-") or "-WA" not in filename:
            return None

        date_str = filename[4:12]
        date_bin = f"{date_str[:4]}:{date_str[4:6]}:{date_str[6:]}"
        return date_bin
    except (ValueError, IndexError):
        return None


class ExifInfoGuesser:
    def get_date_time_original(self, picture: Picture) -> Optional[bytes]:
        path_as_list = get_path_as_list(picture.path)

        guess_attempt = guess_date_bin_from_whatsapp_file(path_as_list)
        if not guess_attempt:
            guess_attempt = guess_date_using_year_month_day_pattern(path_as_list)
        if not guess_attempt:
            guess_attempt = guess_date_using_year_month_pattern(path_as_list)

        if not guess_attempt:
            return None

        date_bin = f"{guess_attempt} 12:34:56".encode("ascii")
        return date_bin
