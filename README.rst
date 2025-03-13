Running the app
===============

.. code-block:: bash

    $ pip install pyinstaller==2.1
    $ pip install exifread
    $ apt-get install python-wxgtk2.8
    $ make compile

Ensure this directory is in contained in $PYTHONPATH (export PYTHONPATH=.:$PYTHONPATH)

.. code-block:: bash

    $ python src/main.py


Most useful commands:
1. python src/main.py report no-exif-date --dir-path "/mnt/c/Users/drime/OneDrive/Pictures/Samsung Gallery/Fotos/"
2. python src/main.py report no-exif-location --dir-path "/mnt/c/Users/drime/OneDrive/Pictures/Samsung Gallery/Fotos/"
3. python src/main.py edit set-exif-date --date "2024:09:25 12:34:57" "/mnt/c/Users/drime/OneDrive/Pictures/Samsung Gallery/Fotos/2024/9. September/20240925"*".jpg"
4. python src/main.py edit set-exif-location -- 54.991008 -2.574939 "/mnt/c/Users/drime/Desktop/smurfs.jpg"