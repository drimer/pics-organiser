from files.manager import PictureManager
from files.picture import Picture, is_image_file


def report_imgs_without_exif_date(path: str, picture_manager: PictureManager) -> list[Picture]:
    images_without_date = []
    
    pictures_collection = picture_manager.find_images(path)
    for picture in pictures_collection:
        if picture.datetime_taken is None:
            images_without_date.append(picture)
    
    return images_without_date


def report_imgs_where_path_date_not_in_exif(path: str, picture_manager: PictureManager) -> list[Picture]:
    images_without_date = []
    
    for picture in picture_manager.find_images(path):
        possible_year = next((part for part in picture.parent_folders_as_list if part.isdigit() and len(part) == 4), None)
        possible_month = next((part for part in picture.parent_folders_as_list if part.isdigit() and len(part) in (1, 2)), None)
        if not possible_month:
            for part in picture.parent_folders_as_list:
                try:
                    possible_month = part.split('.')[0]
                except:
                    pass
        
        if possible_year and possible_month:
            if picture.datetime_taken is None:
                images_without_date.append(picture)
            elif str(picture.datetime_taken.year) != possible_year:
                images_without_date.append(picture)
            elif str(picture.datetime_taken.month) != possible_month:
                images_without_date.append(picture)
            
    return images_without_date