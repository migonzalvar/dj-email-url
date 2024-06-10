<!-- SPDX-FileCopyrightText: 2013-2022 Miguel Gonzalez <migonzalvar@gmail.com> -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Change Log

## Unreleased

## [1.0.6](https://pypi.python.org/pypi/dj-email-url/1.0.6) - 2022-09-24

- Remove unnecessary code (thanks \@matthiask).
- Improve license metadata. No changes on license itself.

## [1.0.5](https://pypi.python.org/pypi/dj-email-url/1.0.5) - 2022-02-05

- Added support for the timeout setting.

## [1.0.4](https://pypi.python.org/pypi/dj-email-url/1.0.4) - 2022-01-16

- Post release version to update change log.

## [1.0.3](https://pypi.python.org/pypi/dj-email-url/1.0.3) - 2022-01-16

- Added support for Python 3.10.
- Changed continuos integration infrastructure from Travis to GitHub
  Actions.
- Switched to PyPA build frontend.

## [1.0.2](https://pypi.python.org/pypi/dj-email-url/1.0.2) - 2021-01-23

- Add support for Python 3.9 (@pauloxnet)

## [1.0.1](https://pypi.python.org/pypi/dj-email-url/1.0.1) - 2020-06-03

- Included LICENSE file in tarball. Thanks to \@fabaff.

## [1.0.0](https://pypi.python.org/pypi/dj-email-url/1.0.0) - 2020-02-16

- Removed support for Python versions which reached end-of-life.
- Fixed typo. Thanks to \@jeffmacdonald.

## [0.2.0](https://pypi.python.org/pypi/dj-email-url/0.2.0) - 2019-04-08

- Added support for `DEFAULT_FROM_EMAIL` and `SERVER_EMAIL` in the URL
  as query parameters.

## [0.1.0](https://pypi.python.org/pypi/dj-email-url/0.1.0) - 2018-03-24

- Added new schemes `submission` and `submit` to select SMTP backend
  on port 587 with STARTTLS. Thanks to \@LEW21 to suggest to include
  new [submit]{.title-ref} URI.
- Discouraged the use of scheme `smtps` and add a user warning. Thanks
  to \@LEW21 to alert about this confusing usage.
- Expand which values are considered as truthy on a query string
  param. Now, [1]{.title-ref}, [on]{.title-ref}, [true]{.title-ref},
  and [yes]{.title-ref}, as a single character or in all case variants
  (lower, upper and title case) are considered as [True]{.title-ref}.

## [0.0.10](https://pypi.python.org/pypi/dj-email-url/0.0.10) - 2016-10-14

- Post release version to fix release date in change log.

## [0.0.9](https://pypi.python.org/pypi/dj-email-url/0.0.9) - 2016-10-14

- Fix case when user sets ssl=False in its url (thanks bogdal)

## [0.0.8](https://pypi.python.org/pypi/dj-email-url/0.0.8) - 2016-06-07

- Allow universal wheel

## [0.0.7](https://pypi.python.org/pypi/dj-email-url/0.0.7) - 2016-05-31

- Add EMAIL_USE_SSL setting to docs and set a default value (thanks
  iraycd).
- Add coverage (thanks iraycd).

## [0.0.6](https://pypi.python.org/pypi/dj-email-url/0.0.6) - 2016-04-18

- Fix error parsing URL without credentials (thanks martinmaillard).

## [0.0.5](https://pypi.python.org/pypi/dj-email-url/0.0.5) - 2016-04-17

- Allow URL encoded credentials (thanks kane-c).

## [0.0.4](https://pypi.python.org/pypi/dj-email-url/0.0.4) - 2015-03-05

- Fix README.

## [0.0.3](https://pypi.python.org/pypi/dj-email-url/0.0.3) - 2015-03-05

- Add change log.
- Add `ssl=` option as a query parameter for SMTP backend.
- Add Travis continuous integration.

## [0.0.2](https://pypi.python.org/pypi/dj-email-url/0.0.2) - 2014-03-12

- Add Python 3 support.

## [0.0.1](https://pypi.python.org/pypi/dj-email-url/0.0.1) - 2013-02-12

- Initial version.
