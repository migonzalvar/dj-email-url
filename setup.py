# -*- coding: utf-8 -*-

from setuptools import setup


with open('README.rst') as f:
    long_description = f.read()

setup(
    name='dj-email-url',
    version='0.0.9',
    url='https://github.com/migonzalvar/dj-email-url',
    license='BSD',
    author='Miguel Gonzalez',
    author_email='migonzalvar@gmail.com',
    description='Use an URL to configure email backend settings in your '
                'Django Application.',
    long_description=long_description,
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
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
