# !/usr/bin/env python

from distutils.core import setup, find_packages

setup(
    name='Template',
    version='0.1dev',
    packages=['template', find_packages()],
    license='',
    long_description=open('README.md').read(),
)