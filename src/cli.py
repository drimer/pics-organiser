import click

from exif_info.guessers import ExifInfoGuesser
from files.manager import PictureManager
from tasks.editors import (
    set_exif_date,
    set_exif_date_to_best_guess,
)
from tasks.reports import (
    PictureReporter,
    PictureReporterByExifDateNotInPath,
    PictureReporterByExifDateNotInWhatsappFileName,
    PictureReporterByMissingExifDate,
    PictureReporterByMissingExifLocation,
    find_and_report_imgs,
)


@click.group()
def cli():
    pass


@cli.group()
def report():
    pass


@report.command("no-exif-date")
@click.argument("path", type=click.Path(exists=True))
def no_exif_date_cli(path: str):
    for result in find_and_report_imgs(
        path, (PictureReporterByMissingExifDate(),), PictureManager()
    ):
        print(f"{result[0]} - {result[1].description}")


@report.command("no-exif-location")
@click.argument("path", type=click.Path(exists=True))
def no_exif_location_cli(path: str):
    for result in find_and_report_imgs(
        path, (PictureReporterByMissingExifLocation(),), PictureManager()
    ):
        print(f"{result[0]} - {result[1].description}")


@report.command("exif-date-not-in-path")
@click.argument("path", type=click.Path(exists=True))
def exif_date_not_in_path_cli(path: str):
    for result in find_and_report_imgs(
        path,
        (
            PictureReporterByExifDateNotInPath(),
            PictureReporterByExifDateNotInWhatsappFileName(),
        ),
        PictureManager(),
    ):
        print(f"{result[0]} - {result[1].description}")


@report.command("all")
@click.argument("path", type=click.Path(exists=True))
def report_all_cli(path: str):
    all_reporters_cls = PictureReporter.__subclasses__()

    for result in find_and_report_imgs(
        path,
        [reporter_cls() for reporter_cls in all_reporters_cls],
        PictureManager(),
    ):
        print(f"{result[0]} - {result[1].description}")


@cli.group()
def edit():
    pass


@edit.command("set-exif-date")
@click.option("--date", help="Date to set in the format YYYY:MM:DD")
@click.argument("file_paths", nargs=-1, type=click.Path(exists=True))
def set_exif_date_cli(date: str, file_paths: list[str]):
    for file_path in file_paths:
        set_exif_date(file_path, date, PictureManager())
        print(f"File {file_path} got changed to {date}")


@edit.command("set-exif-date-to-best-guess")
@click.option(
    "--overwrite",
    is_flag=True,
    default=False,
    help="Whether to overwrite existing EXIF date",
)
@click.argument("paths", nargs=-1, type=click.Path(exists=True))
def set_exif_date_to_best_guess_cli(overwrite: bool, paths: list[str]):
    for path in paths:
        files_changed = set_exif_date_to_best_guess(
            overwrite, path, PictureManager(), ExifInfoGuesser()
        )
        for file_changed in files_changed:
            print(f"File {file_changed[0]} got changed to {file_changed[1]}")
