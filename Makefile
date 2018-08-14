# Options:
# - TARGET_OS   One of: osx, windows, linux.

OS := TARGET_OS

ifeq ($(OS),osx)
	EXTRA_ARGS := --windowed
endif
ifeq ($(OS),windows)
	EXTRA_ARGS := --windowed
endif
ifeq ($(OS),linux)
	EXTRA_ARGS :=
endif


requirements:
	pip install -r requirements/build.txt

requirements-dev:
	pip install -r requirements/dev.txt

unit-tests:
	nosetests -v

lint:
	git ls-files *.py | xargs -n 1 pylint --rcfile=extra/pylintrc .

test: requirements-dev unit-tests lint

compile: requirements-dev
	pyinstaller --clean -F src/main.py --hidden-import PyQt5.sip $(EXTRA_ARGS)

clean:
	find . -name "*.pyc" | xargs -n 1 rm -v
	rm -rf build/ dist/ main.spec
