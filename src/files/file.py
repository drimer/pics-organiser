import os
import shutil
import datetime


class File:
    def __init__(self, path):
        self.path = path

    def __repr__(self):
        return self.path

    @property
    def filename(self):
        return os.path.basename(self.path)

    @property
    def size(self):
        return os.path.getsize(self.path)

    @property
    def last_modified(self):
        return datetime.datetime.fromtimestamp(os.path.getmtime(self.path))

    def copy(self, dest_path):
        target_dirname = os.path.dirname(dest_path)
        if not os.path.exists(target_dirname):
            os.makedirs(target_dirname)

        shutil.copy(self.path, dest_path)