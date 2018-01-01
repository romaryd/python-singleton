# -*- coding: utf8 -*-
"""
Metaclass to easily define singleton classes
"""
__version__ = '0.1.2'


class Singleton(type):
    """
    Usage:
        class bar(object, metaclass=Singleton):
    or
        class bar(object):
            __metaclass__ = Singleton
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton,
                                        cls).__call__(*args, **kwargs)
        return cls._instances[cls]
