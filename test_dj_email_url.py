#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import unittest

import dj_email_url


class EmailTestSuite(unittest.TestCase):
    def test_smtps_parsing(self):
        url = 'smtps://user@domain.com:password@smtp.example.com:587'
        url = dj_email_url.parse(url)

        assert url['EMAIL_BACKEND'] == \
            'django.core.mail.backends.smtp.EmailBackend'
        assert url['EMAIL_HOST'] == 'smtp.example.com'
        assert url['EMAIL_HOST_PASSWORD'] == 'password'
        assert url['EMAIL_HOST_USER'] == 'user@domain.com'
        assert url['EMAIL_PORT'] == 587
        assert url['EMAIL_USE_TLS'] is True
        assert url['EMAIL_USE_SSL'] is False

    def test_console_parsing(self):
        url = 'console://'
        url = dj_email_url.parse(url)

        assert url['EMAIL_BACKEND'] == \
            'django.core.mail.backends.console.EmailBackend'
        assert url['EMAIL_HOST'] is None
        assert url['EMAIL_HOST_PASSWORD'] is None
        assert url['EMAIL_HOST_USER'] is None
        assert url['EMAIL_PORT'] is None
        assert url['EMAIL_USE_TLS'] is False
        assert url['EMAIL_USE_SSL'] is False

    def test_email_url(self):
        a = dj_email_url.config()
        assert not a

        os.environ['EMAIL_URL'] = \
            'smtps://user@domain.com:password@smtp.example.com:587'

        url = dj_email_url.config()

        assert url['EMAIL_BACKEND'] == \
            'django.core.mail.backends.smtp.EmailBackend'
        assert url['EMAIL_HOST'] == 'smtp.example.com'
        assert url['EMAIL_HOST_PASSWORD'] == 'password'
        assert url['EMAIL_HOST_USER'] == 'user@domain.com'
        assert url['EMAIL_PORT'] == 587
        assert url['EMAIL_USE_TLS'] is True
        assert url['EMAIL_USE_SSL'] is False

    def test_smtp_backend_smtp_scheme_default_port(self):
        url = 'smtp://user@domain.com:pass@smtp.example.com'
        url = dj_email_url.parse(url)
        assert url['EMAIL_PORT'] == 25
        assert url['EMAIL_USE_SSL'] is False
        assert url['EMAIL_USE_TLS'] is False

    def test_smtp_backend_submit_scheme_default_port(self):
        # Included in README
        url = 'submit://user@exmple.com:pass@smtp.example.com'
        url = dj_email_url.parse(url)
        assert url['EMAIL_PORT'] == 587
        assert url['EMAIL_USE_SSL'] is False
        assert url['EMAIL_USE_TLS'] is True

    def test_smtp_backend_submission_scheme_default_port(self):
        # Included in README
        url = 'submission://user@exmple.com:pass@smtp.example.com'
        url = dj_email_url.parse(url)
        assert url['EMAIL_PORT'] == 587
        assert url['EMAIL_USE_SSL'] is False
        assert url['EMAIL_USE_TLS'] is True

    def test_smtp_backend_with_smpt_over_ssl(self):
        url = 'smtp://user@domain.com:pass@smtp.example.com:465/?ssl=True'
        url = dj_email_url.parse(url)
        assert url['EMAIL_PORT'] == 465
        assert url['EMAIL_USE_SSL'] is True
        assert url['EMAIL_USE_TLS'] is False

    def test_smtp_backend_local_mta(self):
        # Included in README
        url = 'smtp://'
        url = dj_email_url.parse(url)
        assert url['EMAIL_HOST'] == 'localhost'
        assert url['EMAIL_PORT'] == 25
        assert url['EMAIL_USE_SSL'] is False
        assert url['EMAIL_USE_TLS'] is False

    def test_smtp_backend_without_ssl(self):
        url = 'smtp://user@domain.com:pass@smtp.example.com:465/?ssl=False'
        url = dj_email_url.parse(url)
        assert url['EMAIL_USE_SSL'] is False
        assert url['EMAIL_USE_TLS'] is False

    def test_smtps_backend_with_ssl(self):
        url = 'smtps://user@domain.com:pass@smtp.example.com:465/?ssl=True'
        url = dj_email_url.parse(url)
        assert url['EMAIL_USE_SSL'] is True
        assert url['EMAIL_USE_TLS'] is False

    def test_smtp_backend_with_tls(self):
        url = 'smtp://user@domain.com:pass@smtp.example.com:587/?tls=True'
        url = dj_email_url.parse(url)
        assert url['EMAIL_USE_SSL'] is False
        assert url['EMAIL_USE_TLS'] is True

    def test_smtp_backend_without_tls(self):
        url = 'smtp://user@domain.com:pass@smtp.example.com:587/?tls=False'
        url = dj_email_url.parse(url)
        assert url['EMAIL_USE_SSL'] is False
        assert url['EMAIL_USE_TLS'] is False

    def test_special_chars(self):
        url = 'smtp://user%21%40%23%245678:pass%25%5E%26%2A%28%29123@' \
              'smtp.example.com:587'
        url = dj_email_url.parse(url)
        assert url['EMAIL_HOST_PASSWORD'] == 'pass%^&*()123'
        assert url['EMAIL_HOST_USER'] == 'user!@#$5678'

    def test_file_path(self):
        url = 'smtp://user@domain.com:pass@smtp.example.com:587' \
              '//tmp/app-messages?tls=True'
        url = dj_email_url.parse(url)
        assert url['EMAIL_FILE_PATH'] == "/tmp/app-messages"
        assert url['EMAIL_USE_SSL'] is False
        assert url['EMAIL_USE_TLS'] is True


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
