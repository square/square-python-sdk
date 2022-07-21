# -*- coding: utf-8 -*-

import sys
from setuptools import setup, find_packages

if sys.version_info[0] < 3:
    with open('README.md', 'r') as fh:
        long_description = fh.read()
else:
    with open('README.md', 'r', encoding='utf-8') as fh:
        long_description = fh.read()

setup(
    name='squareup',
    version='20.1.0.20220720',
    description='Use Square APIs to manage and run business including payment, customer, product, inventory, and employee management.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Square Developer Platform',
    author_email='developers@squareup.com',
    url='https://squareup.com/developers',
    packages=find_packages(),
    install_requires=[
        'jsonpickle~=1.4, >= 1.4.1',
        'requests~=2.25',
        'cachecontrol~=0.12.6',
        'python-dateutil~=2.8.1',
        'deprecation~=2.1'
    ],
    tests_require=[
        'nose>=1.3.7'
    ],
    test_suite = 'nose.collector'
)