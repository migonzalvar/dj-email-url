#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import unittest

import dj_email_url


class EmailTestSuite(unittest.TestCase):
    def test_smtp_parsing(self):
        url = 'smtps://user@domain.com:password@smtp.example.com:587'
        url = dj_email_url.parse(url)

        assert url['EMAIL_BACKEND'] == \
            'django.core.mail.backends.smtp.EmailBackend'
        assert url['EMAIL_HOST'] == 'smtp.example.com'
        assert url['EMAIL_HOST_PASSWORD'] == 'password'
        assert url['EMAIL_HOST_USER'] == 'user@domain.com'
        assert url['EMAIL_PORT'] == 587
        assert url['EMAIL_USE_TLS'] is True

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

    def test_smtp_backend_with_ssl(self):
        url = 'smtp://user@domain.com:pass@smtp.example.com:465/?ssl=True'
        url = dj_email_url.parse(url)
        assert url['EMAIL_USE_SSL'] is True
        assert url['EMAIL_USE_TLS'] is False

    def test_smtp_backend_with_tls(self):
        url = 'smtp://user@domain.com:pass@smtp.example.com:587/?tls=True'
        url = dj_email_url.parse(url)
        assert url['EMAIL_USE_SSL'] is False
        assert url['EMAIL_USE_TLS'] is True

    def test_special_chars(self):
        url = 'smtp://user%21%40%23%245678:pass%25%5E%26%2A%28%29123@' \
              'smtp.example.com:587'
        url = dj_email_url.parse(url)
        assert url['EMAIL_HOST_PASSWORD'] == 'pass%^&*()123'
        assert url['EMAIL_HOST_USER'] == 'user!@#$5678'

if __name__ == '__main__':
    unittest.main()
