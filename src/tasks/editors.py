from typing import Generator

import piexif

from files.manager import PictureManager
from exif_info.guessers import ExifInfoGuesser


def set_exif_date_to_best_guess(
    overwrite: bool,
    path: str,
    picture_manager: PictureManager,
    exif_info_guesser: ExifInfoGuesser,
) -> Generator[tuple, None, None]:
    for picture in picture_manager.find_images(path):
        # Do not overwrite existing date if not explicitly allowed
        if (
            picture.exif_metadata["Exif"].get(piexif.ExifIFD.DateTimeOriginal)
            and not overwrite
        ):
            continue

        date_bin = exif_info_guesser.get_date_time_original(picture)
        if not date_bin:
            print(f"Could not guess date for {picture.path}, skipping")
            continue

        picture.exif_metadata["Exif"][piexif.ExifIFD.DateTimeOriginal] = date_bin
        exif_bytes = piexif.dump(picture.exif_metadata)

        picture_manager.save(picture, picture.path, "jpeg", exif=exif_bytes)

        yield (picture.path, date_bin)


def set_exif_date(file_path: str, date: str, picture_manager: PictureManager):
    picture = picture_manager.get_image(file_path)
    picture.datetime_taken = date.encode("ascii")
    exif_bytes = piexif.dump(picture.exif_metadata)

    picture_manager.save(picture, picture.path, "jpeg", exif=exif_bytes)
