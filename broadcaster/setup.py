#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This software is licensed as described in the README.rst and LICENSE
# files, which you should have received as part of this distribution.

import codecs
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from broadcaster.__init__ import __version__ as VERSION

DESCRIPTION = 'Library to easily use multiple types notifications'

with codecs.open('README.rst', 'r', encoding='UTF-8') as readme:
    LONG_DESCRIPTION = ''.join(readme)

CLASSIFIERS = [
    'Environment :: Console',
    'Intended Audience :: System Administrators',
    'Operating System :: Unix',
    'Operating System :: POSIX :: Linux',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Topic :: Communications',
    'Topic :: Utilities'
]

packages = [
    'broadcaster',
]

setup(
    name = 'broadcaster',
    version = VERSION,
    description = DESCRIPTION,
    long_description = LONG_DESCRIPTION,
    author = 'Richard Kellmer',
    author_email = 'richard.kellner [at] erigones.com',
    url = 'https://github.com/ricco386/broadcaster/',
    license = '',
    packages = packages,
    scripts = ['bin/broadcaster'],
    install_requires = ['pushnotify'],
    platforms = 'Linux',
    classifiers = CLASSIFIERS,
    include_package_data = True
)