from typing import Generator, List

import piexif

from files.manager import PictureManager
from files.picture import get_path_as_list


def guess_date_using_year_month_day_pattern(path_as_list: List[str]):
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


def guess_date_using_year_month_pattern(path_as_list: List[str]):
    month_dir_name = path_as_list[-1]
    year_dir_name = path_as_list[-2]

    month_first_chars = month_dir_name.split(".")[0]
    month_str = f"{int(month_first_chars):0>2}"

    if int(year_dir_name) > 1988 and int(month_str) > 12:
        return None

    return f"{year_dir_name}:{month_str}:15"


def guess_date_bin_from_full_path(path_as_list: List[str]):
    guess_attempt = guess_date_using_year_month_day_pattern(path_as_list)
    if not guess_attempt:
        guess_attempt = guess_date_using_year_month_pattern(path_as_list)

    date_bin = f"{guess_attempt} 12:34:56".encode("ascii")
    return date_bin


def convert_dd_location_to_dms(decimal_degrees: float, seconds_precision):
    abs_decimal_degrees = abs(decimal_degrees)

    dms_degrees = int(abs_decimal_degrees)
    degrees_leftover = abs_decimal_degrees - dms_degrees
    dms_minutes = int(degrees_leftover * 60)
    minutes_leftover = degrees_leftover * 60 - dms_minutes
    # import pdb

    # pdb.set_trace()
    # csec = ((minsec % 60) / float(3600)) * (10**11)
    dms_seconds = int(minutes_leftover * 60 * seconds_precision)
    return dms_degrees, dms_minutes, dms_seconds


def convert_dd_pair_location_to_piexif_gps_dms(dd1: float, dd2: float) -> dict:
    precision = 10**6

    return {
        1: b"N" if dd1 >= 0 else b"S",
        2: (
            (convert_dd_location_to_dms(dd1, precision)[0], 1),
            (convert_dd_location_to_dms(dd1, precision)[1], 1),
            (convert_dd_location_to_dms(dd1, precision)[2], precision),
        ),
        3: b"E" if dd2 >= 0 else b"W",
        4: (
            (convert_dd_location_to_dms(dd2, precision)[0], 1),
            (convert_dd_location_to_dms(dd2, precision)[1], 1),
            (convert_dd_location_to_dms(dd2, precision)[2], precision),
        ),
        5: 0,
        6: (1, 1),
    }


def set_exif_date_from_path(
    path: str, picture_manager: PictureManager
) -> Generator[tuple, None, None]:
    print(f"===> Setting dates from path {path}")

    for picture in picture_manager.find_images(path):
        # Do not overwrite existing date
        if picture.exif_metadata["Exif"].get(piexif.ExifIFD.DateTimeOriginal):
            continue

        date_bin = guess_date_bin_from_full_path(get_path_as_list(picture.path))

        picture.exif_metadata["Exif"][piexif.ExifIFD.DateTimeOriginal] = date_bin
        exif_bytes = piexif.dump(picture.exif_metadata)

        picture_manager.save(picture, picture.path, "jpeg", exif=exif_bytes)

        yield (picture.path, date_bin)


def set_exif_date(file_path: str, date: str, picture_manager: PictureManager):
    picture = picture_manager.get_image(file_path)
    picture.datetime_taken = date.encode("ascii")
    exif_bytes = piexif.dump(picture.exif_metadata)

    picture_manager.save(picture, picture.path, "jpeg", exif=exif_bytes)


def set_exif_gps_location(
    file_path: str, dms_location: dict, picture_manager: PictureManager
):
    picture = picture_manager.get_image(file_path)
    picture.exif_metadata["GPS"] = dms_location
    exif_bytes = piexif.dump(picture.exif_metadata)

    picture_manager.save(picture, picture.path, "jpeg", exif=exif_bytes)
