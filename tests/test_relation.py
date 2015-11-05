import unittest
from unittest.mock import MagicMock
from random import random

from formalarg import Relation

def rand():
    return random() < 0.5

class TestRelation(unittest.TestCase):
    @unittest.skip("Not implemented")
    def test_init(self):
        self.fail("Not Implemented")

    @unittest.skip("Not implemented")
    def test_add_supporters(self):
        self.fail("Not Implemented")

    @unittest.skip("Not implemented")
    def test_add_opponants(self):
        self.fail("Not Implemented")

    @unittest.skip("Not implemented")
    def test_support_difference(self):
        self.fail("Not Implemented")

    def test_is_present(self):
        arg1 = MagicMock()
        arg1.is_present.return_value = False
        arg2 = MagicMock()
        arg2.is_present.return_value = True
        rel = Relation(arg1, arg2, 1)
        self.assertFalse(rel.is_present())
        arg1.is_present.return_value = True
        self.assertTrue(rel.is_present())

        rel.probability = 0.5
        sum = 0.0
        for i in range(100000):
            if rel.is_present():
                sum += 1
        sum /= 100000.0
        self.assertAlmostEquals(sum, 0.5, 2)

        arg2.is_present = rand
        sum = 0.0
        for i in range(100000):
            if rel.is_present():
                sum += 1
        sum /= 100000.0
        self.assertAlmostEquals(sum, 0.25, 2)
