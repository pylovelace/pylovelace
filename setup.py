#!/usr/local/bin/python3.11

from setuptools import setup, find_packages
from os import path

directory = path.abspath(path.dirname(__file__))

with open(path.join(directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='PyIntellect',
      version='0.0.1',
      description='Python code obfuscation tool',
      long_description=long_description,
      author='nshout',
      url='https://pyintellect.com/',
      classifiers=[
          'Development Status :: 1 - Planning',
          'Intended Audience :: Developers',
          'Programming Language :: Python :: 3',
          'Operating System :: Microsoft :: Windows',
      ],
      packages=find_packages(),
      entry_points={'console_scripts': ['pyintellect=pyintellect.pyintellect:main']}
      )
