from collections import defaultdict
from PIL import Image
import click
import piexif
import os
import glob

from cli import cli

from files.picture import is_image_file


def report_imgs_without_exif_date(path: str, ):
    print('===> Starting report')
    
    paths_list = glob.glob(f"{path}\\**\\*", recursive=True)
    files_list = [path for path in paths_list if os.path.isfile(path)]
    total = 0
    
    for file_path in files_list:
        if not is_image_file(file_path):
            continue

        try:
            img = Image.open(file_path)
        except:
            print(f"Something wrong with {file_path}")
            continue

        if 'exif' not in img.info:
            total += 1
            print(file_path)
    
    print(f"Total: {total}")
    