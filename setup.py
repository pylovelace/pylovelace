"""
PyIntellect
Python Obfuscation Tool

Copyright 2023 PyIntellect

Author - nshout
"""
from setuptools import setup
from os import path
from source import __version__, __description__

directory = path.abspath(path.dirname(__file__))

with open(path.join(directory, 'source', 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='PyLovelace',
    version=__version__,
    description=__description__,
    long_description=long_description,
    author='nshout',
    url='https://github.com/pylovelace/pylovelace',
    keywords='obfuscate obfuscation distribute production tool',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'Topic :: Security',
        'Programming Language :: Python :: 3.11',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'Operating System :: Microsoft :: Windows :: Windows 11',
    ],
    packages=[
        'pylovelace',
    ],
    package_dir={
        'pylovelace': 'source',
    },
    package_data={
        'pylovelace': [
            '*.py',
        ]
    },
    install_requires=[
        'pylovelace.kernel',
        'cryptography',
        'requests',
        'tqdm',
    ],
    setup_requires=[
        'wheel'
    ],
    entry_points={
        'console_scripts': [
            'pylovelace=pylovelace.__main__:main'
        ]
    }
)
