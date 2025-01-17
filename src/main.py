import glob
import os
from collections import defaultdict

import piexif
from PIL import Image

from cli import cli


def is_image_file(path):
    return path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.webp'))


def set_exif_date_in_path_with_hardcoded_date(path, date_bin):
    print(f"===> Setting hardcoded date {date_bin} in {path}")

    paths_list = glob.glob(f"{path}\\**\\*", recursive=True)
    files_list = [path for path in paths_list if os.path.isfile(path)]
    for file_path in files_list:
        if not is_image_file(file_path):
            continue

        try:
            img = Image.open(file_path)
        except:
            print(f"Something wrong with {file_path}")
            continue

        if 'exif' not in img.info:
            exif_dict = defaultdict(dict)
        else:
            try:
                exif_dict = piexif.load(img.info['exif'])
            except:
                print(f"Could not load exif for {file_path}")
                continue

        # Do not overwrite existing date
        if exif_dict['Exif'].get(piexif.ExifIFD.DateTimeOriginal):
            continue

        exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal] = date_bin
        exif_bytes = piexif.dump(exif_dict)

        try:
            img.save(file_path, "jpeg", exif=exif_bytes)
        except:
            print(f"Could not save {file_path}")
            continue


if __name__ == "__main__":
    cli()

# if __name__ == "__main__":
# set_exif_date_from_path("C:\\Users\\drime\\Desktop\\test_pics")

# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2005\\1. Enero', b"2005:01:31 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2005\\2. Febrero', b"2005:02:28 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2005\\3. Marzo', b"2005:03:31 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2005\\4. Abril', b"2005:04:30 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2005\\5. Mayo', b"2005:05:31 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2005\\6. Junio', b"2005:06:30 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2005\\7. Julio', b"2005:07:31 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2005\\8. Agosto', b"2005:08:31 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2005\\9. Septiembre', b"2005:09:30 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2005\\10. Octubre', b"2005:10:31 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2005\\11. Noviembre', b"2005:11:30 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2005\\12. Diciembre', b"2005:12:31 23:59:59")

# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2008\\3. Marzo', b"2008:03:31 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2008\\4. Abril', b"2008:04:30 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2008\\5. Mayo', b"2008:05:31 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2008\\6. Junio', b"2008:06:30 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2008\\7. Julio', b"2008:07:31 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2008\\8. Agosto', b"2008:08:31 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2008\\9. Septiembre', b"2008:09:30 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2008\\10. Octubre', b"2008:10:31 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2008\\11. Noviembre', b"2008:11:30 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2008\\12. Diciembre', b"2008:12:31 23:59:59")

# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2009\\2. Febrero', b"2009:02:28 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2008\\3. Marzo', b"2009:03:31 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2009\\4. Abril', b"2009:04:30 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2009\\5. Mayo', b"2009:05:31 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2009\\6. Junio', b"2009:06:30 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2009\\7. Julio', b"2009:07:31 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2009\\8. Agosto', b"2009:08:31 23:59:59")

# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2010\\1. Enero', b"2010:01:31 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2010\\2. Febrero', b"2010:02:28 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2010\\3. Marzo', b"2010:03:31 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2010\\4. Abril', b"2010:04:30 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2010\\5. Mayo', b"2010:05:31 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2010\\6. Junio', b"2010:06:30 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2010\\7. Julio', b"2010:07:31 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2010\\8. Agosto', b"2010:08:31 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2010\\9. Septiembre', b"2010:09:30 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2010\\10. Octubre', b"2010:10:31 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2010\\11. Noviembre', b"2010:11:30 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2010\\12. Diciembre', b"2010:12:31 23:59:59")

# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2011\\1. Enero', b"2011:01:31 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2011\\2. Febrero', b"2011:02:28 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2011\\3. Marzo', b"2011:03:31 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2011\\4. Abril', b"2011:04:30 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2011\\5. Mayo', b"2011:05:31 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2011\\6. Junio', b"2011:06:30 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2011\\7. Julio', b"2011:07:31 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2011\\8. Agosto', b"2011:08:31 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2011\\9. Septiembre', b"2011:09:30 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2011\\10. Octubre', b"2011:10:31 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2011\\11. Noviembre', b"2011:11:30 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2011\\12. Diciembre', b"2011:12:31 23:59:59")

# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2012\\1. Enero', b"2012:01:31 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2012\\2. Febrero', b"2012:02:29 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2012\\3. Marzo', b"2012:03:31 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2012\\4. Abril', b"2012:04:30 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2012\\5. Mayo', b"2012:05:31 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2012\\6. Junio', b"2012:06:30 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2012\\7. Julio', b"2012:07:31 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2012\\8. Agosto', b"2012:08:31 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2012\\9. Septiembre', b"2012:09:30 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2012\\10. Octubre', b"2012:10:31 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2012\\11. Noviembre', b"2012:11:30 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2012\\12. Diciembre', b"2012:12:31 23:59:59")

# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2013\\1. Enero', b"2013:01:31 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2013\\2. Febrero', b"2013:02:28 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2013\\3. Marzo', b"2013:03:31 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2013\\4. Abril', b"2013:04:30 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2013\\5. Mayo', b"2013:05:31 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2013\\6. Junio', b"2013:06:30 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2013\\7. Julio', b"2013:07:31 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2013\\8. Agosto', b"2013:08:31 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2013\\9. Septiembre', b"2013:09:30 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2013\\10. Octubre', b"2013:10:31 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2013\\11. Noviembre', b"2013:11:30 23:59:59")
# set_exif_date_in_path_with_hardcoded_date('C:\\Users\\drime\\Desktop\\test_pics\\2013\\12. Diciembre', b"2013:12:31 23:59:59")

# for year in ('2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024'):
#     set_exif_date_in_path_with_hardcoded_date(f'C:\\Users\\drime\\Desktop\\test_pics\\{year}\\1. January', f"{year}:01:31 23:59:59".encode("ascii"))
#     set_exif_date_in_path_with_hardcoded_date(f'C:\\Users\\drime\\Desktop\\test_pics\\{year}\\2. February', f"{year}:02:28 23:59:59".encode("ascii"))
#     set_exif_date_in_path_with_hardcoded_date(f'C:\\Users\\drime\\Desktop\\test_pics\\{year}\\3. March', f"{year}:03:31 23:59:59".encode("ascii"))
#     set_exif_date_in_path_with_hardcoded_date(f'C:\\Users\\drime\\Desktop\\test_pics\\{year}\\4. April', f"{year}:04:30 23:59:59".encode("ascii"))
#     set_exif_date_in_path_with_hardcoded_date(f'C:\\Users\\drime\\Desktop\\test_pics\\{year}\\5. May', f"{year}:05:31 23:59:59".encode("ascii"))
#     set_exif_date_in_path_with_hardcoded_date(f'C:\\Users\\drime\\Desktop\\test_pics\\{year}\\6. June', f"{year}:06:30 23:59:59".encode("ascii"))
#     set_exif_date_in_path_with_hardcoded_date(f'C:\\Users\\drime\\Desktop\\test_pics\\{year}\\7. July', f"{year}:07:31 23:59:59".encode("ascii"))
#     set_exif_date_in_path_with_hardcoded_date(f'C:\\Users\\drime\\Desktop\\test_pics\\{year}\\8. August', f"{year}:08:31 23:59:59".encode("ascii"))
#     set_exif_date_in_path_with_hardcoded_date(f'C:\\Users\\drime\\Desktop\\test_pics\\{year}\\9. September', f"{year}:09:30 23:59:59".encode("ascii"))
#     set_exif_date_in_path_with_hardcoded_date(f'C:\\Users\\drime\\Desktop\\test_pics\\{year}\\10. October', f"{year}:10:31 23:59:59".encode("ascii"))
#     set_exif_date_in_path_with_hardcoded_date(f'C:\\Users\\drime\\Desktop\\test_pics\\{year}\\11. November', f"{year}:11:30 23:59:59".encode("ascii"))
#     set_exif_date_in_path_with_hardcoded_date(f'C:\\Users\\drime\\Desktop\\test_pics\\{year}\\12. December', f"{year}:12:31 23:59:59".encode("ascii"))

# report_imgs_without_exif_date("C:\\Users\\drime\\Desktop\\test_pics")
