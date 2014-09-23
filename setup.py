from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name             = 'tornado-smtp',
    version          = '0.1.0',
    description      = 'An asynchronous SMTP client for Tornado',
    long_description = long_description,
    url              = 'https://github.com/rmoritz/tornado-smtp',
    author           = 'Ralph Moritz',
    author_email     = 'ralphmoritz@outlook.com',
    license          = 'MIT',
    keywords         = ['smtp', 'email', 'mail', 'tornado', 'async'],
    packages         = ['tornado_smtp'],
    classifiers      = [
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4'
    ],
)
