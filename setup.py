#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 2020

@author: Scott Tuttle
"""

from pathlib import Path
from setuptools import setup, find_packages

with open('README.rst', 'r') as readme:
    long_description = readme.read()


def get_version(rel_path):
    target_path = Path(__file__).resolve().parent.joinpath(rel_path)
    with open(target_path, 'r') as file:
        for line in file:
            if line.startswith('__version__'):
                delimiter = '"' if '"' in line else "'"
                return line.split(delimiter)[1]
        else:
            raise RuntimeError("Unable to find version string.")


setup(
      name='scottbrian_secdata',
      version=get_version('src/scottbrian_secdata/__init__.py'),
      author='Scott Tuttle',
      description='Obtain fundamental data from SEC data dump txt files',
      long_description=long_description,
      long_description_content_type='text/x-rst',
      url='https://github.com/ScottBrian/scottbrian_secdata.git',
      license='MIT',
      classifiers=[
          'License :: OSI Approved :: MIT License',
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'Intended Audience :: Financial and Insurance Industry',
          'Topic :: Office/Business :: Financial :: Investment',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.8',
          'Operating System :: POSIX :: Linux'
                  ],
      project_urls={
          'Documentation': 'https://scottbrian-secdata.readthedocs.io/en'
                           '/latest/',
          'Source': 'https://github.com/ScottBrian/scottbrian_secdata.git'},
      python_requires='>=3.8',
      packages=['scottbrian_secdata'],
      package_dir={'': 'src'},
      install_requires=['pandas', 'scottbrian_utils', 'pip>=21.1.1'],
      package_data={"scottbrian_secdata": ["__init__.pyi", "py.typed"]},
      zip_safe=False
     )
