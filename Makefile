default: test

install:
	python -m venv .venv
	.venv/bin/python -m pip install --upgrade pip setuptools wheel
	.venv/bin/python -m pip install docutils pygments
	.venv/bin/python -m pip install build twine check-wheel-contents

release: clean test build
	.venv/bin/check-wheel-contents dist/*.whl
	@echo
	@echo Upload to PyPI
	@echo twine upload dist/*

test: install
	.venv/bin/python test_dj_email_url.py
	.venv/bin/rst2html.py README.rst --halt=info >/dev/null

build: install
	.venv/bin/python -m build --sdist --wheel .

clean:
	rm -f README.rst.html
	rm -f dist/*
