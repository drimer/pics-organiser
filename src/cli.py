import click

from files.manager import PictureManager
from tasks.editors import set_exif_date, set_exif_date_from_path
from tasks.reports import (
    report_imgs_where_path_date_not_in_exif,
    report_imgs_without_exif_date,
)


@click.group()
def cli():
    pass


@cli.group()
def report():
    pass


@report.command()
@click.option("--dir-path", help="Path to the folder with the images")
def no_exif(dir_path):
    for img in report_imgs_without_exif_date(dir_path, PictureManager()):
        print(img)


@report.command()
@click.option("--dir-path", help="Path to the folder with the images")
def date_not_in_path(dir_path):
    for img in report_imgs_where_path_date_not_in_exif(dir_path, PictureManager()):
        print(img)


@cli.group()
def edit():
    pass


@edit.command()
@click.option("--dir-path", help="Path to the folder with the images")
def set_exif_date_to_best_guess(dir_path):
    files_changed = set_exif_date_from_path(dir_path, PictureManager())
    for file_changed in files_changed:
        print(f"File {file_changed[0]} got changed to {file_changed[1]}")


@edit.command("set-exif-date")
@click.option("--date", help="Date to set in the format YYYY:MM:DD")
@click.argument("file_paths", nargs=-1)
def set_exif_date_cli(date, file_paths):
    for file_path in file_paths:
        set_exif_date(file_path, date, PictureManager())
