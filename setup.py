#!/usr/bin/env python

from setuptools import setup

setup(
    name='ckanexport',
    version='0.1-alpha',
    description=
        'A tool for exporting data from CKAN in a friendly format',
    license='MIT',
    author='U.S. Open Data Institute',
    author_email='contact@boxkite.ca',
    url='https://github.com/opendata/CKAN-Export',
    packages=[
        'ckanexport',
        ],
    test_suite='',
    zip_safe=False,
    entry_points = """
        [console_scripts]
        ckanexport=ckanexport.cli:main

        [paste.paster_command]
        ckanexport=ckanexport.paster:CKANExportCommand
        """
    )
