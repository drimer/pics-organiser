import glob
import os
from typing import Generator

from PIL import Image

from files.picture import Picture, is_image_file


class PictureFinder(object):

    def __init__(self, path):
        assert os.path.isdir(path)

        self.path = path

    def find_all(self):
        for root, _, files in os.walk(self.path):
            for filename in files:
                abs_path = os.path.join(root, filename)
                if is_image_file(abs_path):
                    yield Picture(abs_path)


class PictureManager:
    def find_images(self, path) -> Generator[Picture, None, None]:
        paths_list = glob.iglob(f"{path}/**/*", recursive=True)
        files_list = (path for path in paths_list if os.path.isfile(path))

        for file_path in files_list:
            if not is_image_file(file_path):
                continue

            # TODO: Pull this out into separate report so I can know what images
            # it fails to open
            try:
                Image.open(file_path)
            except:
                print(f"Something wrong with {file_path}")
                continue

            yield Picture(file_path)

    def get_image(self, path):
        return Picture(path)

    def save(self, picture: Picture, path: str, format: str, exif: any):
        img = Image.open(picture.path)
        img.save(path, format, exif=exif)
