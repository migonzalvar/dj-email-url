default: test

test:
	python3 test_dj_email_url.py
	rst2html.py README.rst --halt=info >/dev/null

clean:
	rm -f README.rst.html
	rm -f dist/*

release: test clean
	python3 setup.py sdist bdist_wheel
	@echo
	@echo Upload to PyPI
	@echo twine upload dist/*
