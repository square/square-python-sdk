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
    version='8.1.0.20210121',
    description='Use Square APIs to manage and run business including payment, customer, product, inventory, and employee management.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Square Developer Platform',
    author_email='developers@squareup.com',
    url='https://squareup.com/developers',
    packages=find_packages(),
    install_requires=[
        'requests>=2.9.1, <3.0',
        'jsonpickle>=0.7.1, <1.0',
        'cachecontrol>=0.11.7, <1.0',
        'python-dateutil>=2.5.3, <3.0',
        'deprecation>=2.0.6'
    ],
    tests_require=[
        'nose>=1.3.7'
    ],
    test_suite = 'nose.collector'
)