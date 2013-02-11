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
    EMAIL_USE_TLS = email_config['EMAIL_USE_TLS']


Supported backends
------------------

Currently, it supports:

- SMTP backend (smtp and smtps),

- console backend (console),

- file backend (file),

- in-memory backend (memory),

- and dummy backend (dummy).

The scheme ``smtps`` indicates to use TLS connections, that is to set
``EMAIL_USE_TLS`` to ``True``.

The file backend is the only one which needs a path. The url path is store
in ``EMAIL_FILE_PATH`` key.
