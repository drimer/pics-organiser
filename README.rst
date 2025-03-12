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
1. python src/main.py report no-exif --dir-path "/mnt/usb/DCIM/100CANON"
2. python src/main.py edit set-exif-date --date "2025:04:08 12:34:56" "some/images"*".jpg"
