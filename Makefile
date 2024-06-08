# SPDX-FileCopyrightText: 2013-2022 Miguel Gonzalez <migonzalvar@gmail.com>
#
# SPDX-License-Identifier: CC0-1.0

PYTHON := .venv/bin/python

default: test

install:
	python -m venv .venv
	${PYTHON} -m pip install --upgrade pip setuptools wheel
	${PYTHON} -m pip install docutils pygments
	${PYTHON} -m pip install build twine check-wheel-contents

release: clean test build
	@echo Check:
	@echo ''
	@echo '[ ] Change log updated.'
	@echo '[ ] Version bumped (bumpversion patch).'
	@echo '[ ] Updated GitHub (git push).'
	@echo ''
	@echo 'Finally:'
	@echo ''
	@echo '[ ] Upload to PyPI (twine upload dist/*).'

test: install
	${PYTHON} test_dj_email_url.py
	${PYTHON} -m docutils README.rst --halt=info >/dev/null
	${PYTHON} -m docutils CHANGELOG.rst --halt=info >/dev/null

build: install
	${PYTHON} -m build --sdist --wheel .
	${PYTHON} -m check_wheel_contents dist/*.whl

clean:
	rm -f README.rst.html
	rm -f dist/*
