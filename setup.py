#!/usr/bin/env python

# Release process:
#
#  - set version in IPy/__init__.py
#  - set version in setup.py
#  - set version in README.rst
#  - run unit test: make
#  - set release date in ChangeLog
#  - git commit -a
#  - git tag -a IPy-x.y -m "tag IPy x.y"
#  - git push
#  - git push --tags
#  - python setup.py register sdist upload
#
# After the release:
#  - set version to n+1 (IPy/__init__.py and setup.py)
#  - add a new empty section in the changelog for version n+1
#  - git commit -a
#  - git push

from setuptools import setup

VERSION = '1.2'

options = {}

with open('README.rst') as fp:
    README = fp.read().strip() + "\n\n"

ChangeLog = (
    "What's new\n"
    "==========\n"
    "\n")
with open('ChangeLog') as fp:
    ChangeLog += fp.read().strip()

LONG_DESCRIPTION = README
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
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3.12',
    'Programming Language :: Python :: 3.13',
    'Programming Language :: Python :: 3.14',
    'Typing :: Typed',
]
URL = "https://github.com/autocracy/python-ipy"

setup(
    name="IPy",
    version=VERSION,
    description="Class and tools for handling of IPv4 and IPv6 addresses and networks",
    long_description=LONG_DESCRIPTION,
    author="Maximillian Dornseif",
    maintainer="Jeff Ferland",
    maintainer_email="jeff_ipy@storyinmemo.com",
    license="BSD License",
    keywords="ipv4 ipv6 netmask",
    url=URL,
    download_url=URL,
    classifiers=CLASSIFIERS,
    packages=["IPy"],
    package_data={"IPy": ["py.typed"]},
    python_requires=">=3.5",
    test_suite="test.test_IPy",
    **options
)
