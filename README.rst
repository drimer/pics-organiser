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
