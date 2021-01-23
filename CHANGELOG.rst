Change Log
==========

Unreleased
----------

1.0.2_ - 2021-01-23
-------------------

.. _1.0.2: https://pypi.python.org/pypi/dj-email-url/1.0.2

- Add support for Python 3.9 (@pauloxnet)

1.0.1_ - 2020-06-03
-------------------

.. _1.0.1: https://pypi.python.org/pypi/dj-email-url/1.0.1

- Included LICENSE file in tarball. Thanks to @fabaff.

1.0.0_ - 2020-02-16
-------------------

.. _1.0.0: https://pypi.python.org/pypi/dj-email-url/1.0.0

- Removed support for Python versions which reached end-of-life.

- Fixed typo. Thanks to @jeffmacdonald.

0.2.0_ - 2019-04-08
-------------------

.. _0.2.0: https://pypi.python.org/pypi/dj-email-url/0.2.0

- Added support for ``DEFAULT_FROM_EMAIL`` and ``SERVER_EMAIL`` in the URL as
  query parameters.

0.1.0_ - 2018-03-24
-------------------

.. _0.1.0: https://pypi.python.org/pypi/dj-email-url/0.1.0

- Added new schemes ``submission`` and ``submit``
  to select SMTP backend on port 587 with STARTTLS.
  Thanks to @LEW21 to suggest to include new `submit` URI.

- Discouraged the use of scheme ``smtps`` and add a user warning.
  Thanks to @LEW21 to alert about this confusing usage.

- Expand which values are considered as truthy on a query string param. Now,
  `1`, `on`, `true`, and `yes`, as a single character or in all case variants
  (lower, upper and title case) are considered as `True`.

0.0.10_ - 2016-10-14
--------------------

- Post release version to fix release date in change log.

0.0.9_ - 2016-10-14
-------------------

- Fix case when user sets ssl=False in its url (thanks bogdal)

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
.. _0.0.10: https://pypi.python.org/pypi/dj-email-url/0.0.10
