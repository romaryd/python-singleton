# Singleton Metaclass

[![Build Status](https://travis-ci.org/romaryd/python-singleton.svg?branch=master)](https://travis-ci.org/romaryd/python-singleton)
[![Coverage Status](https://coveralls.io/repos/github/romaryd/python-singleton/badge.svg?branch=master)](https://coveralls.io/github/romaryd/python-singleton?branch=master)
[![Maintainability](https://api.codeclimate.com/v1/badges/b03f759c2a1d62011a6d/maintainability)](https://codeclimate.com/github/romaryd/python-singleton/maintainability)
[![Code Health](https://landscape.io/github/romaryd/python-singleton/master/landscape.svg?style=flat)](https://landscape.io/github/romaryd/python-singleton/master)

## Installation

```
pip install python-singleton
```

## Usage

Python 2.7:

```python
class bar(object):
    __metaclass__ = Singleton
```

Python 3.6:
```python
class bar(object, metaclass=Singleton):
```
