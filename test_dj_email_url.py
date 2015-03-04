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


if __name__ == '__main__':
    unittest.main()
