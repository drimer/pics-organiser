all:

check: check-tests check-pylint

check-tests:
	nosetests -v

check-pylint:
	git ls-files *.py | xargs -n 1 pylint --rcfile=extra/pylintrc .
