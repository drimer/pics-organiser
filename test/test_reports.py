from datetime import datetime
import mock
from files.manager import PictureManager
from tasks.reports import report_imgs_without_exif_date


def test_report_imgs_without_exif_date_nothing_found():
    pictureManagerMock = mock.MagicMock()
    pictureManagerMock.find_images.return_value = []
    
    result = report_imgs_without_exif_date('./test/files', pictureManagerMock)
    
    assert result == []


def test_report_imgs_without_exif_date_one_image_found():
    pictureManagerMock = mock.MagicMock()
    pictureManagerMock.find_images.return_value = [
        mock.MagicMock(datetime_taken=None, path='test1.jpg'),
        mock.MagicMock(datetime_taken=datetime(2024, 4, 4, 14, 50) , path='test2.jpg'),
    ]
    
    result = report_imgs_without_exif_date('./test/files', pictureManagerMock)
    
    assert result == [pictureManagerMock.find_images.return_value[0]]
    

def test_report_imgs_without_exif_date_no_matches():
    pictureManagerMock = mock.MagicMock()
    pictureManagerMock.find_images.return_value = [
        mock.MagicMock(datetime_taken=datetime(2024, 4, 8, 14, 50), path='test1.jpg'),
        mock.MagicMock(datetime_taken=datetime(2024, 4, 4, 14, 50), path='test2.jpg'),
    ]
    
    result = report_imgs_without_exif_date('./test/files', pictureManagerMock)
    
    assert result == []