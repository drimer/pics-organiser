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


.PHONY: requirements
requirements:
	pip install -r requirements/build.txt

.PHONY: requirements-dev
requirements-dev:
	pip install -r requirements/dev.txt

.PHONY: unit-tests
unit-tests:
	nosetests -v

.PHONY: lint
lint:
	git ls-files *.py | xargs -n 1 pylint --rcfile=extra/pylintrc .

.PHONY: test
test: requirements-dev unit-tests lint

compile: requirements-dev
	pyinstaller --clean -F src/main.py --hidden-import PyQt5.sip $(EXTRA_ARGS)

clean:
	find . -name "*.pyc" | xargs -n 1 rm -v
	rm -rf build/ dist/ main.spec
