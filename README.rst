============
dj-email-url
============

.. image:: https://badge.fury.io/py/dj-email-url.svg
    :target: http://badge.fury.io/py/dj-email-url

This utility is based on dj-database-url by Kenneth Reitz.

It allows to utilize the
`12factor <http://www.12factor.net/backing-services>`_ inspired
environments variable to configure the email backend in a Django application.

Usage
=====

Import the package in ``settings.py``:

.. code:: python

    import dj_email_url


Fetch your email configuration values. The default option is fetch them from
``EMAIL_URL`` environment variable:

.. code:: python

    email_config = dj_email_url.config()

Other option is parse an arbitrary email URL:

.. code:: python

    email_config = dj_email_url.parse('smtp://...')


Finally, it is **necessary** to assign values to settings:

.. code:: python

    EMAIL_FILE_PATH = email_config['EMAIL_FILE_PATH']
    EMAIL_HOST_USER = email_config['EMAIL_HOST_USER']
    EMAIL_HOST_PASSWORD = email_config['EMAIL_HOST_PASSWORD']
    EMAIL_HOST = email_config['EMAIL_HOST']
    EMAIL_PORT = email_config['EMAIL_PORT']
    EMAIL_BACKEND = email_config['EMAIL_BACKEND']
    EMAIL_USE_TLS = email_config['EMAIL_USE_TLS']
    EMAIL_USE_SSL = email_config['EMAIL_USE_SSL']

Alternatively, it is possible to use this less explicit shortcut:

.. code:: python

    vars().update(email_config)

Supported backends
==================

Currently, it supports:

- SMTP backend (smtp and smtps for TLS),

- console backend (console),

- file backend (file),

- in-memory backend (memory),

- and dummy backend (dummy).

SMTP backend
------------

The scheme ``smtps`` indicates to use TLS connections, that is to set
``EMAIL_USE_TLS`` to ``True``.

It is possible to specify SSL using a `ssl=True` as a query parameter:

.. code:: pycon

    >>> url = 'smtp://user@domain.com:pass@smtp.example.com:465/?ssl=True'
    >>> url = dj_email_url.parse(url)
    >>> assert url['EMAIL_USE_SSL'] is True

File backend
------------

The file backend is the only one which needs a path. The url path is store
in ``EMAIL_FILE_PATH`` key.

Change Log
==========

0.0.9_ - Unreleased
-------------------

- Fixcase when user sets ssl=False in its url (thanks bogdal)

0.0.8_ - 2016-06-07
-------------------

- Allow universal wheel

0.0.7_ - 2016-05-31
-------------------

- Add EMAIL_USE_SSL setting to docs and set a default value (thanks iraycd).
- Add coverage (thanks iraycd).

0.0.6_ - 2016-04-18
-------------------

- Fix error parsing URL without credentials (thanks martinmaillard).

0.0.5_ - 2016-04-17
-------------------

- Allow URL encoded credentials (thanks kane-c).

0.0.4_ - 2015-03-05
-------------------

- Fix README.

0.0.3_ - 2015-03-05
-------------------

- Add change log.

- Add `ssl=` option as a query parameter for SMTP backend.

- Add Travis continuous integration.

0.0.2_ - 2014-03-12
-------------------

- Add Python 3 support.

0.0.1_ - 2013-02-12
-------------------

- Initial version.

.. _0.0.1: https://pypi.python.org/pypi/dj-email-url/0.0.1
.. _0.0.2: https://pypi.python.org/pypi/dj-email-url/0.0.2
.. _0.0.3: https://pypi.python.org/pypi/dj-email-url/0.0.3
.. _0.0.4: https://pypi.python.org/pypi/dj-email-url/0.0.4
.. _0.0.5: https://pypi.python.org/pypi/dj-email-url/0.0.5
.. _0.0.6: https://pypi.python.org/pypi/dj-email-url/0.0.6
.. _0.0.7: https://pypi.python.org/pypi/dj-email-url/0.0.7
.. _0.0.8: https://pypi.python.org/pypi/dj-email-url/0.0.8
.. _0.0.9: https://pypi.python.org/pypi/dj-email-url/0.0.9

CI status
=========

Development (master):

.. image:: https://travis-ci.org/migonzalvar/dj-email-url.svg?branch=master
  :target: http://travis-ci.org/migonzalvar/dj-email-url

.. image:: https://codecov.io/gh/migonzalvar/dj-email-url/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/migonzalvar/dj-email-url
