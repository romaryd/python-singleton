"""
Test singleton Metaclass
"""

import unittest
from six import add_metaclass
from singleton import Singleton


class SingletonTests(unittest.TestCase):
    """
    Singleton Metaclass utility tests.
    """

    def test_singleton(self):
        """
        Test the singleton Metaclass
        """
        @add_metaclass(Singleton)
        class IntSingleton(object):

            def __init__(self, default=0):
                self.i = default

        a = IntSingleton(10)
        b = IntSingleton(10)

        self.assertEqual(a, b)
        self.assertEqual(id(a), id(b))
        self.assertEqual(a.i, 10)
        self.assertEqual(b.i, 10)
        a.i = 100
        self.assertEqual(b.i, 100)
