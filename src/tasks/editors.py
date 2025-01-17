import os

import piexif

from files.manager import PictureManager
from files.picture import get_path_as_list


def guess_date_using_year_month_day_pattern(path_as_list: list[str]):
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


def guess_date_using_year_month_pattern(path_as_list: list[str]):
    month_dir_name = path_as_list[-1]
    year_dir_name = path_as_list[-2]

    month_first_chars = month_dir_name.split(".")[0]
    month_str = f"{int(month_first_chars):0>2}"

    if int(year_dir_name) > 1988 and int(month_str) > 12:
        return None

    return f"{year_dir_name}:{month_str}:15"


def guess_date_bin_from_full_path(path_as_list: list[str]):
    guess_attempt = guess_date_using_year_month_day_pattern(path_as_list)
    if not guess_attempt:
        guess_attempt = guess_date_using_year_month_pattern(path_as_list)

    date_bin = f"{guess_attempt} 12:34:56".encode("ascii")
    return date_bin


def set_exif_date_from_path(path: str, picture_manager: PictureManager) -> list[tuple]:
    print(f"===> Setting dates from path {path}")
    edited_pictures = []

    for picture in picture_manager.find_images(path):
        # Do not overwrite existing date
        if picture.exif_metadata['Exif'].get(piexif.ExifIFD.DateTimeOriginal):
            continue

        date_bin = guess_date_bin_from_full_path(get_path_as_list(picture.path))

        picture.exif_metadata['Exif'][piexif.ExifIFD.DateTimeOriginal] = date_bin
        exif_bytes = piexif.dump(picture.exif_metadata)

        picture_manager.save(picture, picture.path, "jpeg", exif=exif_bytes)

        edited_pictures.append((picture.path, date_bin))

    return edited_pictures
