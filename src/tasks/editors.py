import os

import piexif

from files.manager import PictureManager


def get_date_bin_from_full_path(path):
    day_dir_path = os.path.dirname(path)
    day_dir_name = os.path.basename(day_dir_path)
    month_dir_path = os.path.dirname(day_dir_path)
    month_dir_name = os.path.basename(month_dir_path)
    year_dir_path = os.path.dirname(month_dir_path)
    year_dir_name = os.path.basename(year_dir_path)

    month_first_chars = month_dir_name.split(".")[0]
    month_str = f"{int(month_first_chars):0>2}"

    day_first_chars_possible_range = day_dir_name.split(".")[0]
    if "-" in day_first_chars_possible_range:
        day_first_chars = day_first_chars_possible_range.split("-")[0]
    else:
        day_first_chars = day_first_chars_possible_range
    day_str = f"{int(day_first_chars):0>2}"

    # The above can atch a lot of weird things. Verify that the date is valid
    if int(year_dir_name) > 1988 and int(month_str) > 12 or int(day_str) > 31:
        raise ValueError("Invalid date")

    date_str = f"{year_dir_name}:{month_str}:{day_str}"
    date_bin = f"{date_str} 12:34:56".encode("ascii")
    return date_bin


def set_exif_date_from_path(path: str, picture_manager: PictureManager) -> list[tuple]:
    print(f"===> Setting dates from path {path}")
    edited_pictures = []

    for picture in picture_manager.find_images(path):
        # Do not overwrite existing date
        if picture.exif_metadata['Exif'].get(piexif.ExifIFD.DateTimeOriginal):
            continue

        try:
            date_bin = get_date_bin_from_full_path(picture.path)
        except:
            try:
                date_bin = get_date_bin_from_full_path(os.path.dirname(picture.path))
            except:
                continue

        picture.exif_metadata['Exif'][piexif.ExifIFD.DateTimeOriginal] = date_bin
        exif_bytes = piexif.dump(picture.exif_metadata)

        picture_manager.save(picture, picture.path, "jpeg", exif=exif_bytes)

        edited_pictures.append((picture.path, date_bin))

    return edited_pictures
