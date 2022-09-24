# SPDX-FileCopyrightText: 2013-2022 Miguel Gonzalez <migonzalvar@gmail.com>
#
# SPDX-License-Identifier: CC0-1.0

default: test

install:
	python -m venv .venv
	.venv/bin/python -m pip install --upgrade pip setuptools wheel
	.venv/bin/python -m pip install docutils pygments
	.venv/bin/python -m pip install build twine check-wheel-contents

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
	.venv/bin/python test_dj_email_url.py
	.venv/bin/rst2html.py README.rst --halt=info >/dev/null
	.venv/bin/rst2html.py CHANGELOG.rst --halt=info >/dev/null

build: install
	.venv/bin/python -m build --sdist --wheel .
	.venv/bin/check-wheel-contents dist/*.whl

clean:
	rm -f README.rst.html
	rm -f dist/*
