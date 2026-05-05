Installing the app
==================

1. Install UV: https://docs.astral.sh/uv/getting-started/installation/

2. Install all dependencies:

.. code-block:: bash

        $ uv sync --all-extras
        $ uv run python --version
        Python 3.10.11


Setting up development environment
==================================

1. Install UV: https://docs.astral.sh/uv/getting-started/installation/

2. Install all dependencies:

.. code-block:: bash

        $ uv sync --all-extras
        $ uv run python --version
        Python 3.10.11

3. Running unit tests:

.. code-block:: bash

    $ uv run pytest

5. Linting:

.. code-block:: bash

    $ uv run flake8 src test --count --max-complexity=10 --max-line-length=120 --show-source --statistics


6. Install the package into your system in editable mode:

.. code-block:: bash

    $ uv tool install . -e
    $ pics-org --help

