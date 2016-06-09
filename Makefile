default: test

test:
	python test_dj_email_url.py
	rst2html README.rst --halt=info >/dev/null

clean:
	rm -f README.rst.html
	rm -f dist/*

release: test clean
	bumpversion patch && git log -1 -p
	python setup.py sdist bdist_wheel
	@echo
	@echo Upload to PyPI
	@echo python -m twine upload dist/*
