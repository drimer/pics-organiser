import os
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
    def find_images(self, path):
        image_finder = PictureFinder(path)
        return image_finder.find_all()

    def get_image(self, name):
        return Image.open(os.path.join)