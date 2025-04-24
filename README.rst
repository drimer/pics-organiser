Running the app
===============

.. code-block:: bash

    $ pipx install .
    $ pics-org --help


Setting up development environment
==================================

Ensure you are using the right Python version:

1. Install PyEnv: https://github.com/pyenv/pyenv or  https://github.com/pyenv-win/pyenv-win/

2. Install the required Python version: 3.10.11 and ensure you activate it:

.. code-block:: bash

        $ pyenv local 3.10.11
        $ python --version
        Python 3.10.11

3. Create a virtual environment:

.. code-block:: bash

    $ python -m venv .venv
    $ .\.venv\Scripts\activate
    $ pip install -r .\requirements-dev.txt

4. Running unit tests:

.. code-block:: bash

    $ pytest

5. Linting:

.. code-block:: bash

    $ flake8 src test

6. Install the package into your system in editable mode:

.. code-block:: bash

    $ python -m pip install --user pipx
    $ pipx install . --editable
    $ pipx run pip install -r requirements-dev.txt


Most useful commands
====================

Most of these use Powershell syntax for path, and some with bash syntax):
1. python src/main.py report no-exif-date --dir-path "C:/Users/drime/OneDrive/Pictures/Samsung Gallery/Fotos/"
2. python src/main.py report no-exif-location --dir-path "C:/Users/drime/OneDrive/Pictures/Samsung Gallery/Fotos/"
3. python src/main.py report exif-date-not-in-path --dir-path "C:/Users/drime/OneDrive/Pictures/Samsung Gallery/Fotos/"
4. python src/main.py edit set-exif-date --date "2024:09:25 12:34:57" "C:/Users/drime/OneDrive/Pictures/Samsung Gallery/Fotos/2024/9. September/20240925/*.jpg"
5. python src/main.py edit set-exif-location -- 54.991008 -2.574939 "/mnt/c/Users/drime/Desktop/smurfs"*".jpg"