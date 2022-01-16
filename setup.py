# -*- coding: utf-8 -*-
"""Packaging implementation"""
from os.path import dirname, join
from setuptools import setup


def read_file(filename):
    with open(join(dirname(__file__), filename)) as file:
        return file.read()


setup(
    name='dj-email-url',
    version='1.0.4',
    url='https://github.com/migonzalvar/dj-email-url',
    license='BSD',
    author='Miguel Gonzalez',
    author_email='migonzalvar@gmail.com',
    description='Use an URL to configure email backend settings in your '
                'Django Application.',
    long_description=read_file('README.rst') + '\n'
                + read_file('CHANGELOG.rst'),
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
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
