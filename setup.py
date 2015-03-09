from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name             = 'tornado-smtp',
    version          = '0.1.1',
    description      = 'An asynchronous SMTP client for Tornado',
    long_description = long_description,
    url              = 'https://github.com/rmoritz/tornado-smtp',
    author           = 'Ralph Moritz',
    author_email     = 'ralphmoritz@outlook.com',
    license          = 'MIT',
    keywords         = ['smtp', 'email', 'mail', 'tornado', 'async'],
    packages         = ['tornado_smtp'],
    install_requires = ['tornado >= 3.2.0'],
    classifiers      = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Environment :: Web Environment',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Communications :: Email',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4'
        'Programming Language :: Python :: 2.7'
    ],
)
