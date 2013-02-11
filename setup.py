# -*- coding: utf-8 -*-
"""
dj-email-url
~~~~~~~~~~~~

This utiliy is based on dj-database-url by Kenneth Reitz.

It allows to utilize the
`12factor <http://www.12factor.net/backing-services>`_ inspired
environments variable to configure the email backend in a Django application.

Usage
-----

Configure your email configuration values in ``settings.py`` from
``EMAIL_URL``::

    email_config = dj_email_url.config()

Parse an arbitrary email URL::

    email_config = dj_email_url.parse('smtp://...')


After this, it is necessary to assign values to settings::

    EMAIL_FILE_PATH = email_config['EMAIL_FILE_PATH']
    EMAIL_HOST_USER = email_config['EMAIL_HOST_USER']
    EMAIL_HOST_PASSWORD = email_config['EMAIL_HOST_PASSWORD']
    EMAIL_HOST = email_config['EMAIL_HOST']
    EMAIL_PORT = email_config['EMAIL_PORT']
    EMAIL_BACKEND = email_config['EMAIL_BACKEND']


Supported backends
------------------

Currently, it supports:

- SMTP backend (smtp or smtps),

- console backend (console),

- file backend (file),

- in-memory backend (memory),

- and dummy backend (dummy).


The scheme ``smtps`` indicates to use TLS connections, that is to set
``EMAIL_USE_TLS`` to ``True``.

The file backend is the only one which needs a path. The url path is store
in ``EMAIL_FILE_PATH`` key.
"""

from setuptools import setup

setup(
    name='dj-email-url',
    version='0.0.1',
    url='https://github.com/migonzalvar/dj-email-url',
    license='BSD',
    author='Miguel Gonzalez',
    author_email='migonzalvar@gmail.com',
    description='Use an URL to configure email backend settings in your Django Application.',
    long_description=__doc__,
    py_modules=['dj_email_url'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
