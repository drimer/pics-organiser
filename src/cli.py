import click

from files.manager import PictureManager
from tasks.editors import set_exif_date, set_exif_date_from_path, set_exif_location
from tasks.reports import (
    report_imgs_where_path_date_not_in_exif,
    report_imgs_without_exif_date,
    report_imgs_without_exif_location,
)


@click.group()
def cli():
    pass


@cli.group()
def report():
    pass


@report.command("no-exif-date")
@click.option("--dir-path", help="Path to the folder with the images")
def date_not_in_exif(dir_path):
    for img in report_imgs_without_exif_date(dir_path, PictureManager()):
        print(img)


@report.command("no-exif-location")
@click.option("--dir-path", help="Path to the folder with the images")
def location_not_in_exif(dir_path):
    for img in report_imgs_without_exif_location(dir_path, PictureManager()):
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


@edit.command("set-exif-location")
@click.argument("location", nargs=2)
@click.argument("file_paths", nargs=-1)
def set_exif_location_cli(location, file_paths):
    location_as_dms = dd2dms(float(location[0]), float(location[1]))
    for file_path in file_paths:
        set_exif_location(file_path, location_as_dms, PictureManager())


def dd2dms(dd1, dd2, ndec=6):
    """Convert a decimal degree coordinate pair to a six-tuple of degrees, minutes seconds.

    The returned values are not rounded.

    Arguments

    dd1, dd2 - coordinate pair, in decimal degrees

    Example

      >>> dd2dms(-74.25,32.1)
      (-74, 15, 6.9444444444444444e-05, 32, 6, 2.7777777777778172e-05)
    """

    # Author: Curtis Price, http://profile.usgs.gov/cprice
    # Disclaimer: Not approved by USGS. (Provisional, subject to revision.)
    def ToDMS(dd, ndec):
        dd1 = abs(float(dd))
        cdeg = int(dd1)
        minsec = dd1 - cdeg
        cmin = int(minsec * 60)
        csec = ((minsec % 60) / float(3600)) * (10**11)
        # if dd < 0:
        #     cdeg = cdeg * -1

        return cdeg, cmin, int(csec)

    try:
        # return a six-tuple
        # return {
        #     1: b"N",
        #     2: ((54, 1), (59, 1), (27627360, 1000000)),
        #     3: b"W",
        #     4: ((2, 1), (34, 1), (29780400, 1000000)),
        #     5: 0,
        #     6: (179, 1),
        # }
        return {
            1: b"N" if dd1 >= 0 else b"S",
            2: (
                (ToDMS(dd1, ndec)[0], 1),
                (ToDMS(dd1, ndec)[1], 1),
                (ToDMS(dd1, ndec)[2], 10**ndec),
            ),
            3: b"E" if dd2 >= 0 else b"W",
            4: (
                (ToDMS(dd2, ndec)[0], 1),
                (ToDMS(dd2, ndec)[1], 1),
                (ToDMS(dd2, ndec)[2], 10**ndec),
            ),
            5: 0,
            6: (1, 1),
        }
    except:
        raise Exception("Invalid input")
