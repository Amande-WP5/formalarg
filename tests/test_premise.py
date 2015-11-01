import unittest

from formalarg import Premise


class TestPremise(unittest.TestCase):
    def test_supports_without_parents(self):
        premise = Premise(1)
        self.assertEqual(premise.supports(), [])


if __name__ == '__main__':
    unittest.main()