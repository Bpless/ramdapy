#!/usr/bin/env python

from distutils.core import setup

setup(
    name='ramda.py',
    version='0.1.6',
    description='Port of ramda into python',
    author='Benjamin Plesser',
    author_email='benjamin.plessser@gmail.com',
    url='https://github.com/bpless/ramda.py/',
    packages=['ramda'],
    package_dir={'ramda': 'src'}
)
