# SPDX-FileCopyrightText: 2013-2022 Miguel Gonzalez <migonzalvar@gmail.com>
#
# SPDX-License-Identifier: CC0-1.0

python := ".venv/bin/python"

default: test

install:
  test -e {{python}} || python -m venv .venv
  {{python}} -m pip install --upgrade pip setuptools

requirements-test: install
  {{python}} -m pip install pytest

requirements-build: install
  {{python}} -m pip install build twine

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

test: requirements-test
  {{python}} -m pytest

build: requirements-build
  {{python}} -m build --sdist .

clean:
  rm -f dist/*
