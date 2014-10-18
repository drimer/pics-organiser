import argparse

from src.picture import PicturesCollection


def parse_args():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--pictures-directory', dest='input_dir')
    parser.add_argument('--dest-directory', dest='output_dir')
    options = parser.parse_args()

    return options


def main():
    opts = parse_args()
    picture_collection = PicturesCollection(opts.input_dir)
    picture_collection.sort_into_folder(opts.output_dir)


if __name__ == '__main__':
    main()
