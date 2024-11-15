from collections import defaultdict
from PIL import Image
import os
import glob

from files.manager import PictureManager
from files.picture import Picture, is_image_file


def report_imgs_without_exif_date(path: str, picture_manager: PictureManager) -> list[Picture]:
    images_without_date = []
    
    pictures_collection = picture_manager.find_images(path)
    for picture in pictures_collection:
        if picture.datetime_taken is None:
            images_without_date.append(picture)
    
    return images_without_date

    