#!/usr/bin/env python

# Release process:
#
#  - set version in IPy.py
#  - set version in setup.py
#  - make (to run tests)
#  - set release date in ChangeLog
#  - git commit -a
#  - git tag -a IPy-x.y -m "tag IPy x.y"
#  - git push
#  - git push --tags
#  - ./setup.py register sdist upload
#  - update the website
#
# After the release:
#  - set version to n+1 (IPy.py and setup.py)
#  - add a new empty section in the changelog for version n+1
#  - git commit -a
#  - git push

from __future__ import with_statement
import sys
from distutils.core import setup

VERSION = '0.76.1'

options = {}

with open('README') as fp:
    README = fp.read().strip() + "\n\n"

ChangeLog = (
    "What's new\n"
    "==========\n"
    "\n")
with open('ChangeLog') as fp:
    ChangeLog += fp.read().strip()

LONG_DESCRIPTION = README + ChangeLog
CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'Environment :: Plugins',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Communications',
    'Topic :: Internet',
    'Topic :: System :: Networking',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Natural Language :: English',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
]
URL = "https://github.com/haypo/python-ipy"

# Python 3: run 2to3
try:
    from distutils.command.build_py import build_py_2to3
except ImportError:
    pass
else:
    options['cmdclass'] = {'build_py': build_py_2to3}

setup(
    name="IPy",
    version=VERSION,
    description="Class and tools for handling of IPv4 and IPv6 addresses and networks",
    long_description=LONG_DESCRIPTION,
    author="Maximillian Dornseif",
    maintainer="Victor Stinner",
    maintainer_email="victor.stinner AT haypocalc.com",
    license="BSD License",
    keywords="ipv4 ipv6 netmask",
    url=URL,
    download_url=URL,
    classifiers= CLASSIFIERS,
    py_modules=["IPy"],
    **options
)

