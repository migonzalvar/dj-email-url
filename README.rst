=============================
dj-email-url |latest-version|
=============================

|travis-ci| |codecov| |python-support|

This utility is based on dj-database-url by Kenneth Reitz.

It allows to utilize the 12factor_ inspired environments variable to
configure the email backend in a Django application.

.. |latest-version| image:: https://img.shields.io/pypi/v/dj-email-url.svg
   :alt: Latest version on PyPI
   :target: https://pypi.org/project/dj-email-url/
.. |travis-ci| image:: https://img.shields.io/travis/migonzalvar/dj-email-url/master.svg
   :alt: Build status
   :target: https://travis-ci.org/migonzalvar/dj-email-url
.. |codecov| image:: https://codecov.io/gh/migonzalvar/dj-email-url/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/migonzalvar/dj-email-url
.. |python-support| image:: https://img.shields.io/pypi/pyversions/dj-email-url.svg
   :target: https://pypi.python.org/pypi/dj-email-url
   :alt: Python versions

.. _12factor: http://www.12factor.net/backing-services

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

Currently, `dj-email-url` supports:

+-----------+--------------------------------------------------+-----------------------------------------------------------+
| Backend   | EMAIL_URL                                        | Description                                               |
+===========+==================================================+===========================================================+
| Console   | ``console:``                                     | Writes to stdout (development)                            |
+-----------+--------------------------------------------------+-----------------------------------------------------------+
| SMTP      | ``smtp:``                                        | Sends using a mail transfer agent at localhost on port 25 |
+-----------+--------------------------------------------------+-----------------------------------------------------------+
| SMTP      | ``submission://USER:PASSWORD@smtp.sendgrid.com`` | Sends using SendGrid_ SMTP on port 587 (STARTTLS)         |
+-----------+--------------------------------------------------+-----------------------------------------------------------+
| File      | ``file:``                                        | Writes to a file                                          |
+-----------+--------------------------------------------------+-----------------------------------------------------------+
| In-memory | ``memory:``                                      |                                                           |
+-----------+--------------------------------------------------+-----------------------------------------------------------+
| Dummy     | ``dummy:``                                       |                                                           |
+-----------+--------------------------------------------------+-----------------------------------------------------------+

.. _SendGrid: https://sendgrid.com/docs/Integrate/Frameworks/django.html


.. warning:: Using special characters on passwords

    To use characters that have a special meaning in an URL (think of ``&``)
    you should use `percent encoding <https://en.wikipedia.org/wiki/Percent-encoding>`_.
    For example, ``m&m`` would become ``m%26m``.

    Because the percent character itself (``%``) serves as the indicator for
    percent-encoded octets, it must be percent-encoded as ``%25``.

    .. code:: pycon

        >>> from urllib.parse import quote_plus
        >>> import dj_email_url
        >>> quote_plus("!@#$%^&*")
        '%21%40%23%24%25%5E%26%2A'
        >>> dj_email_url.parse("smtp://user:%21%40%23%24%25%5E%26%2A@localhost")["EMAIL_HOST_PASSWORD"]
        '!@#$%^&*'


Set from email addresses
========================

`dj-email-url` also supports to optionally specify origin email addreses.

+--------------------+-------------------------+
| Setting            | Query parameter         |
+====================+=========================+
| SERVER_EMAIL       | ``_server_email``       |
+--------------------+-------------------------+
| DEFAULT_FROM_EMAIL | ``_default_from_email`` |
+--------------------+-------------------------+

For example: ``smtp://USER:PASSWORD@smtp.example.com/?_server_email=error@example.com``

Do not forget to assign values to settings:

.. code:: python

    SERVER_EMAIL = email_config.get('SERVER_EMAIL', 'root@localhost')
    DEFAULT_FROM_EMAIL = email_config.get('DEFAULT_FROM_EMAIL', 'webmaster@localhost')


More info
=========

SMTP backend
------------

The `SMTP backend`__ is selected when the scheme in the URL if one these:

__ https://docs.djangoproject.com/en/dev/topics/email/#smtp-backend

============================ ============ =========================
Value                        Default port Comment
============================ ============ =========================
``smtp``                     25           Local mail transfer agent
``submission`` or ``submit`` 587          SMTP with STARTTLS
============================ ============ =========================


*Changed in version 0.1:* The use of ``smtps`` is now discouraged__
The value ``smtps`` was used to indicate to use TLS connections,
that is to set ``EMAIL_USE_TLS`` to ``True``.
Now is recommended to use ``submission`` or ``submit``
(see `service name for port numbers`_ or `Uniform Resource Identifier Schemes`_ at IANA).

__ SMTPS_

.. _SMTPS: https://en.wikipedia.org/wiki/SMTPS

.. _service name for port numbers: https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml?search=587

.. _Uniform Resource Identifier Schemes: https://www.iana.org/assignments/uri-schemes/uri-schemes.xhtml

On the most popular mail configuration option is
to use a **third party SMTP server to relay emails**.

.. code:: pycon

    >>> url = 'submission://user@example.com:pass@smtp.example.com'
    >>> url = dj_email_url.parse(url)
    >>> assert url['EMAIL_PORT'] == 587
    >>> assert url['EMAIL_USE_SSL'] is False
    >>> assert url['EMAIL_USE_TLS'] is True

Other common option is to use a **local mail transfer agent** Postfix or Exim.
In this case it as easy as:

.. code:: pycon

    >>> url = 'smtp://'
    >>> url = dj_email_url.parse(url)
    >>> assert url['EMAIL_HOST'] == 'localhost'
    >>> assert url['EMAIL_PORT'] == 25
    >>> assert url['EMAIL_USE_SSL'] is False
    >>> assert url['EMAIL_USE_TLS'] is False

It is also possible to configure **SMTP-over-SSL** (usually on 465).
This configuration is not generally recommended but might be needed for legacy systems.
To apply use this configuration specify SSL using a `ssl=True` as a query parameter
and indicate the port explicitly:

.. code:: pycon

    >>> url = 'smtp://user@domain.com:pass@smtp.example.com:465/?ssl=True'
    >>> url = dj_email_url.parse(url)
    >>> assert url['EMAIL_PORT'] == 465
    >>> assert url['EMAIL_USE_SSL'] is True
    >>> assert url['EMAIL_USE_TLS'] is False

File backend
------------

The file backend is the only one which needs a path. The url path is store
in ``EMAIL_FILE_PATH`` key.
