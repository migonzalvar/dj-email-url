# -*- coding: utf-8 -*-

import os

try:
    import urlparse
except ImportError:
    import urllib.parse as urlparse


# Register email schemes in URLs.
urlparse.uses_netloc.append('smtp')
urlparse.uses_netloc.append('smtps')
urlparse.uses_netloc.append('submit')
urlparse.uses_netloc.append('console')
urlparse.uses_netloc.append('file')
urlparse.uses_netloc.append('memory')
urlparse.uses_netloc.append('dummy')


DEFAULT_ENV = 'EMAIL_URL'


SCHEMES = {
    'smtp': 'django.core.mail.backends.smtp.EmailBackend',
    'smtps': 'django.core.mail.backends.smtp.EmailBackend',
    'submit': 'django.core.mail.backends.smtp.EmailBackend',
    'console': 'django.core.mail.backends.console.EmailBackend',
    'file': 'django.core.mail.backends.filebased.EmailBackend',
    'memory': 'django.core.mail.backends.locmem.EmailBackend',
    'dummy': 'django.core.mail.backends.dummy.EmailBackend'
}


def unquote(value):
        return urlparse.unquote(value) if value else value


def config(env=DEFAULT_ENV, default=None):
    """Returns a dictionary with EMAIL_* settings from EMAIL_URL."""

    conf = {}

    s = os.environ.get(env, default)

    if s:
        conf = parse(s)

    return conf


def parse(url):
    """Parses an email URL."""

    conf = {}

    url = urlparse.urlparse(url)
    qs = urlparse.parse_qs(url.query)

    # Remove query strings
    path = url.path[1:]
    path = path.split('?', 2)[0]

    # Update with environment configuration
    conf.update({
        'EMAIL_FILE_PATH': path,
        'EMAIL_HOST_USER': unquote(url.username),
        'EMAIL_HOST_PASSWORD': unquote(url.password),
        'EMAIL_HOST': url.hostname,
        'EMAIL_PORT': url.port if url.port else 587 if url.scheme == 'submit' else None,
        'EMAIL_USE_SSL': False,
        'EMAIL_USE_TLS': None,
    })

    if url.scheme in SCHEMES:
        conf['EMAIL_BACKEND'] = SCHEMES[url.scheme]

    if 'ssl' in qs and qs['ssl']:
        if qs['ssl'][0] in ('1', 'true', 'True'):
            conf['EMAIL_USE_SSL'] = True
        elif qs['ssl'][0] in ('0', 'false', 'False'):
            conf['EMAIL_USE_SSL'] = False
    elif 'tls' in qs and qs['tls']:
        if qs['tls'][0] in ('1', 'true', 'True'):
            conf['EMAIL_USE_TLS'] = True
        elif qs['tls'][0] in ('0', 'false', 'False'):
            conf['EMAIL_USE_TLS'] = False

    if conf['EMAIL_USE_TLS'] is None:
        conf['EMAIL_USE_TLS'] = True if not conf['EMAIL_USE_SSL'] and url.scheme in ('submit', 'smtps') else False

    return conf
