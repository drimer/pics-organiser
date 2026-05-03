from tasks.editors import (
    convert_dd_location_to_dms,
    convert_dd_pair_location_to_piexif_gps_dms,
    guess_date_bin_from_full_path,
)


def test_convert_dd_location_to_dms_happy_paths():
    assert convert_dd_location_to_dms(37.7749295, 10**6) == (37, 46, 29746199)
    assert convert_dd_location_to_dms(-122.4194155, 10**6) == (122, 25, 9895799)


def test_convert_dd_pair_location_to_piexif_gps_dms_happy_path_north_west():
    assert convert_dd_pair_location_to_piexif_gps_dms(37.7749295, -122.4194155) == {
        1: b"N",
        2: ((37, 1), (46, 1), (29746199, 1000000)),
        3: b"W",
        4: ((122, 1), (25, 1), (9895799, 1000000)),
        5: 0,
        6: (0, 0),
    }


def test_convert_dd_pair_location_to_piexif_gps_dms_happy_path_north_east():
    assert convert_dd_pair_location_to_piexif_gps_dms(35.661236, 139.697355) == {
        1: b"N",
        2: ((35, 1), (39, 1), (40449600, 1000000)),
        3: b"E",
        4: ((139, 1), (41, 1), (50477999, 1000000)),
        5: 0,
        6: (0, 0),
    }


def test_convert_dd_pair_location_to_piexif_gps_dms_happy_path_south_east():
    assert convert_dd_pair_location_to_piexif_gps_dms(-35.661236, 139.697355) == {
        1: b"S",
        2: ((35, 1), (39, 1), (40449600, 1000000)),
        3: b"E",
        4: ((139, 1), (41, 1), (50477999, 1000000)),
        5: 0,
        6: (0, 0),
    }


def test_convert_dd_pair_location_to_piexif_gps_dms_happy_path_south_west():
    assert convert_dd_pair_location_to_piexif_gps_dms(-35.661236, -139.697355) == {
        1: b"S",
        2: ((35, 1), (39, 1), (40449600, 1000000)),
        3: b"W",
        4: ((139, 1), (41, 1), (50477999, 1000000)),
        5: 0,
        6: (0, 0),
    }


def test_guess_date_bin_from_full_path_happy_path_for_year_month_day():
    assert (
        guess_date_bin_from_full_path(
            ["2023", "10. October", "1. Vienna trip", "IMG_1234.jpg"]
        )
        == b"2023:10:01 12:34:56"
    )


def test_guess_date_bin_from_full_path_happy_path_for_year_month():
    assert (
        guess_date_bin_from_full_path(["2023", "10. October", "IMG_1234.jpg"])
        == b"2023:10:15 12:34:56"
    )


def test_guess_date_bin_from_full_path_happy_path_for_whatsapp_file():
    assert (
        guess_date_bin_from_full_path(
            ["family pics", "cousins", "IMG-20130803-WA0006.jpg"]
        )
        == b"2013:08:03 12:34:56"
    )


def test_guess_date_bin_from_full_path_happy_path_for_whatsapp_file_in_year_month_day():
    assert (
        guess_date_bin_from_full_path(
            ["2023", "10. October", "1. Vienna trip", "IMG-20231001-WA0006.jpg"]
        )
        == b"2023:10:01 12:34:56"
    )


def test_guess_date_bin_from_full_path_no_date_in_path():
    assert (
        guess_date_bin_from_full_path(["family pics", "cousins", "IMG_1234.jpg"])
        is None
    )
