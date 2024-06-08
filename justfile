# SPDX-FileCopyrightText: 2013-2022 Miguel Gonzalez <migonzalvar@gmail.com>
#
# SPDX-License-Identifier: CC0-1.0

python := ".venv/bin/python"

default: test

install:
  python -m venv .venv
  {{python}} -m pip install --upgrade pip setuptools wheel
  {{python}} -m pip install docutils pygments
  {{python}} -m pip install build twine check-wheel-contents

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
  {{python}} test_dj_email_url.py
  {{python}} -m docutils README.rst --halt=info >/dev/null
  {{python}} -m docutils CHANGELOG.rst --halt=info >/dev/null

build: install
  {{python}} -m build --sdist --wheel .
  {{python}} -m check_wheel_contents dist/*.whl

clean:
  rm -f README.rst.html
  rm -f dist/*
