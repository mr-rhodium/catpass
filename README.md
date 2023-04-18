[![PyPI version](https://badge.fury.io/py/p-gen.svg)](https://badge.fury.io/py/p-gen)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)


## About

Cat Pass is **Password Generator** is a console utility that allows you to generate passwords.

***

## Requirements:
* Python 3+

***

## Installation

### Install `password-generator` via pip:

```console
$ pip install cat-pass
```

***

## Usage

Available keywords: `catp catpass cat-pass`

### Examples

```commandline
catp -h

>>>
usage: gen.py [-h] [-length LENGTH] [-seed SEED]
              [-special_symbols SPECIAL_SYMBOLS] [-symbols SYMBOLS]

Smile Password Generator

options:
  -h, --help            show this help message and exit
  -length LENGTH, -len LENGTH, -l LENGTH
                        Specify the length of password
  -seed SEED, -s SEED   Specify a secret key to generate unique
                        passwords
  -special_symbols SPECIAL_SYMBOLS, -ss SPECIAL_SYMBOLS
                        Specify whether to use special symbols like
                        '!#$./:;' etc.
  -symbols SYMBOLS, -ns SYMBOLS
                        Just Alphabet

```commandline
catp

>>> ehp\>tS"gN
```

```commandline
catp -ss 0

>>> sHqYPFlR23
```

```commandline
pgen phrase1 phrase2 -l 20

>>> CwzSbJS3r3\B5Bs_?d$-