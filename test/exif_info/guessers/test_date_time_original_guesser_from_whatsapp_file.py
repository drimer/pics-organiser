import mock

from exif_info.guessers import DateTimeOriginalGuesserFromWhatsappFile


def test_that_get_date_time_original_from_whatsapp_file_happy_path():
    assert (
        DateTimeOriginalGuesserFromWhatsappFile().get(
            mock.Mock(path="family pics/cousins/IMG-20130803-WA0006.jpg")
        )
        == "2013:08:03"
    )


def test_that_get_date_time_original_from_whatsapp_file_no_whatsapp_file():
    assert (
        DateTimeOriginalGuesserFromWhatsappFile().get(
            mock.Mock(path="family pics/cousins/IMG_1234.jpg")
        )
        is None
    )


def test_that_get_date_time_original_from_whatsapp_file_no_date_in_filename():
    assert (
        DateTimeOriginalGuesserFromWhatsappFile().get(
            mock.Mock(path="family pics/cousins/IMG-WA0006.jpg")
        )
        is None
    )
