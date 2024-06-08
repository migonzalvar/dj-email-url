# dj-email-url [![Latest version on PyPI](https://img.shields.io/pypi/v/dj-email-url.svg)](https://pypi.org/project/dj-email-url/)

[![CI status](https://github.com/migonzalvar/dj-email-url/workflows/CI/badge.svg)](https://github.com/migonzalvar/dj-email-url)
[![Python versions](https://img.shields.io/pypi/pyversions/dj-email-url.svg)](https://pypi.python.org/pypi/dj-email-url)

This utility is based on dj-database-url by Kenneth Reitz.

It allows to utilize the
[12factor](http://www.12factor.net/backing-services) inspired
environments variable to configure the email backend in a Django
application.

## Usage

Import the package in `settings.py`:

```python
import dj_email_url
```

Fetch your email configuration values. The default option is fetch them
from `EMAIL_URL` environment variable:

```python
email_config = dj_email_url.config()
```

Other option is parse an arbitrary email URL:

```python
email_config = dj_email_url.parse('smtp://...')
```

Finally, it is **necessary** to assign values to settings:

```python
EMAIL_FILE_PATH = email_config['EMAIL_FILE_PATH']
EMAIL_HOST_USER = email_config['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = email_config['EMAIL_HOST_PASSWORD']
EMAIL_HOST = email_config['EMAIL_HOST']
EMAIL_PORT = email_config['EMAIL_PORT']
EMAIL_BACKEND = email_config['EMAIL_BACKEND']
EMAIL_USE_TLS = email_config['EMAIL_USE_TLS']
EMAIL_USE_SSL = email_config['EMAIL_USE_SSL']
EMAIL_TIMEOUT = email_config['EMAIL_TIMEOUT']
```

Alternatively, it is possible to use this less explicit shortcut:

```python
vars().update(email_config)
```

## Supported backends

Currently, **dj-email-url** supports:

| Backend   | `EMAIL_URL`                                    | Description                                                                                                    |
| --------- | ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| Console   | `console:`                                     | Writes to stdout (development)                                                                                 |
| SMTP      | `smtp:`                                        | Sends using a mail transfer agent at localhost on port 25                                                      |
| SMTP      | `submission://USER:PASSWORD@smtp.sendgrid.com` | Sends using [SendGrid](https://sendgrid.com/docs/Integrate/Frameworks/django.html) SMTP on port 587 (STARTTLS) |
| File      | `file:`                                        | Writes to a file                                                                                               |
| In-memory | `memory:`                                      |                                                                                                                |
| Dummy     | `dummy:`                                       |                                                                                                                |

> [!WARNING] WARNING: Using special characters on passwords
> To use characters that have a special meaning in an URL (think of `&`)
> you should use [percent
> encoding](https://en.wikipedia.org/wiki/Percent-encoding). For example,
> `m&m` would become `m%26m`.
>
> Because the percent character itself (`%`) serves as the indicator for
> percent-encoded octets, it must be percent-encoded as `%25`.
>
> ```pycon
> >>> from urllib.parse import quote_plus
> >>> import dj_email_url
> >>> quote_plus("!@#$%^&*")
> '%21%40%23%24%25%5E%26%2A'
> >>> dj_email_url.parse("smtp://user:%21%40%23%24%25%5E%26%2A@localhost")["EMAIL_HOST_PASSWORD"]
> '!@#$%^&*'
> ```

## Set from email addresses

**dj-email-url** also supports to optionally specify origin
email addresses.

| Setting            | Query parameter       |
| ------------------ | --------------------- |
| SERVER_EMAIL       | `_server_email`       |
| DEFAULT_FROM_EMAIL | `_default_from_email` |

For example:
`smtp://USER:PASSWORD@smtp.example.com/?_server_email=error@example.com`

Do not forget to assign values to settings:

```python
SERVER_EMAIL = email_config.get('SERVER_EMAIL', 'root@localhost')
DEFAULT_FROM_EMAIL = email_config.get('DEFAULT_FROM_EMAIL', 'webmaster@localhost')
```

## Other settings

There are other settings available to set from query param.

| Setting       | Query parameter | Comments         |
| ------------- | --------------- | ---------------- |
| EMAIL_TIMEOUT | `timeout`       | _New in v1.0.5_. |

## More info

### SMTP backend

The [SMTP
backend](https://docs.djangoproject.com/en/dev/topics/email/#smtp-backend)
is selected when the scheme in the URL if one these:

| Value                    | Default port | Comment                   |
| ------------------------ | ------------ | ------------------------- |
| `smtp`                   | 25           | Local mail transfer agent |
| `submission` or `submit` | 587          | SMTP with STARTTLS        |

> [!NOTE] NOTE
> _Changed in version 0.1:_
> The use of `smtps` is now
> [discouraged](https://en.wikipedia.org/wiki/SMTPS) The value `smtps` was
> used to indicate to use TLS connections, that is to set `EMAIL_USE_TLS`
> to `True`. Now is recommended to use `submission` or `submit` (see
> [service name for port
> numbers](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml?search=587)
> or [Uniform Resource Identifier
> Schemes](https://www.iana.org/assignments/uri-schemes/uri-schemes.xhtml)
> at IANA).

On the most popular mail configuration option is to use a **third party
SMTP server to relay emails**.

```pycon
>>> url = 'submission://user@example.com:pass@smtp.example.com'
>>> url = dj_email_url.parse(url)
>>> assert url['EMAIL_PORT'] == 587
>>> assert url['EMAIL_USE_SSL'] is False
>>> assert url['EMAIL_USE_TLS'] is True
```

Other common option is to use a **local mail transfer agent** Postfix or
Exim. In this case it as easy as:

```pycon
>>> url = 'smtp://'
>>> url = dj_email_url.parse(url)
>>> assert url['EMAIL_HOST'] == 'localhost'
>>> assert url['EMAIL_PORT'] == 25
>>> assert url['EMAIL_USE_SSL'] is False
>>> assert url['EMAIL_USE_TLS'] is False
```

It is also possible to configure **SMTP-over-SSL** (usually on 465).
This configuration is not generally recommended but might be needed for
legacy systems. To apply use this configuration specify SSL using a
[ssl=True]{.title-ref} as a query parameter and indicate the port
explicitly:

```pycon
>>> url = 'smtp://user@domain.com:pass@smtp.example.com:465/?ssl=True'
>>> url = dj_email_url.parse(url)
>>> assert url['EMAIL_PORT'] == 465
>>> assert url['EMAIL_USE_SSL'] is True
>>> assert url['EMAIL_USE_TLS'] is False
```

### File backend

The file backend is the only one which needs a path. The url path is
store in `EMAIL_FILE_PATH` key.

## Running the tests

Fork, then clone the repo:

```bash
git clone git@github.com:put-your-user-here/dj-email-url.git
```

Then you can run the tests with the _just_ command runner:

```bash
just test
```

If you don\'t have _just_ installed, you can look in the `justfile` for
the commands that are run.

## License

This work is licensed under several licenses.

- All original source code is licensed under BSD-2-Clause.
- All documentation is licensed under CC-BY-4.0.
- Some configuration and data files are licensed under CC0-1.0.

For more accurate information, check the individual files.

You can check the compliance with [REUSE helper
tool](https://github.com/fsfe/reuse-tool).
