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
    version='23.0.0.20221019',
    description='Use Square APIs to manage and run business including payment, customer, product, inventory, and employee management.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Square Developer Platform',
    author_email='developers@squareup.com',
    url='https://squareup.com/developers',
    packages=find_packages(),
    install_requires=[
        'apimatic-core~=0.1.0',
        'apimatic-core-interfaces~=0.1.0',
        'apimatic-requests-client-adapter~=0.1.0',
        'python-dateutil~=2.8.1',
        'deprecation~=2.1'
    ],
    tests_require=[
        'pytest>=7.1.3'
    ],
)