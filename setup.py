"""
PyIntellect
Python Obfuscation Tool

Copyright 2023 PyIntellect

Author - nshout
"""
from setuptools import setup
from os import path
from source.core import version

directory = path.abspath(path.dirname(__file__))

with open(path.join(directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='PyIntellect',
    version=version,
    description='Python code obfuscation tool',
    long_description=long_description,
    author='nshout',
    url='https://github.com/pyintellect/pyintellect',
    keywords='obfuscate obfuscation distribute production tool',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'Topic :: Security',
        'Programming Language :: Python :: 3',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'Operating System :: Microsoft :: Windows :: Windows 11',
    ],
    packages=['pyintellect', 'pyintellect.core', 'pyintellect.core.cryptography'],
    package_dir={'pyintellect': 'source'},
    package_data={'pyintellect': ['core/*.py', 'core/*.pyd', 'core/cryptography/*.py', 'core/cryptography/*.pyd']},
    entry_points={'console_scripts': ['pyintellect=pyintellect.pyintellect:main']}
)
