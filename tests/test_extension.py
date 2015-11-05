import unittest
from unittest.mock import MagicMock

from formalarg import Extension


class TestExtension(unittest.TestCase):
    def test_init_without_arguments(self):
        extension = Extension()
        self.assertEqual(len(extension.arguments), 0)

    def test_init_with_arguments(self):
        arg1 = MagicMock()
        arg2 = MagicMock()
        extension = Extension(arg1, arg2)
        self.assertEqual(len(extension.arguments), 2)

    def test_add_arguments_without_arguments(self):
        arg1 = MagicMock()
        arg2 = MagicMock()
        extension = Extension(arg1, arg2)
        extension.add_arguments()
        self.assertEqual(len(extension.arguments), 2)

    def test_add_1_argument(self):
        arg1 = MagicMock()
        arg2 = MagicMock()
        arg3 = MagicMock()
        extension = Extension(arg1, arg2)
        extension.add_arguments(arg3)
        self.assertEqual(len(extension.arguments), 3)

    def test_add_more_arguments(self):
        arg1 = MagicMock()
        arg2 = MagicMock()
        arg3 = MagicMock()
        arg4 = MagicMock()
        arg5 = MagicMock()
        extension = Extension(arg1, arg2)
        extension.add_arguments(arg3, arg4, arg5)
        self.assertEqual(len(extension.arguments), 5)

    def test_is_conflicting(self):
        arg1 = MagicMock()
        arg2 = MagicMock()
        arg3 = MagicMock()
        rel12 = MagicMock()
        rel12.relfrom = arg1
        rel12.relto   = arg2

        extension = Extension(arg1, arg2, arg3)
        self.assertFalse(extension.is_conflict_free([rel12]))

    def test_is_conflict_free(self):
        arg1 = MagicMock()
        arg2 = MagicMock()
        arg3 = MagicMock()
        arg4 = MagicMock()
        arg5 = MagicMock()
        rel14 = MagicMock()
        rel14.relfrom = arg1
        rel14.relto   = arg4
        rel52 = MagicMock()
        rel52.relfrom = arg5
        rel52.relto   = arg2
        rel54 = MagicMock()
        rel54.relfrom = arg5
        rel54.relto   = arg4

        extension = Extension(arg1, arg2, arg3)
        self.assertTrue(extension.is_conflict_free([rel14, rel52, rel54]))

    def test_is_admissible(self):
        arg1 = MagicMock()
        arg1.is_acceptable.return_value = True
        arg2 = MagicMock()
        arg2.is_acceptable.return_value = True
        arg3 = MagicMock()
        arg3.is_acceptable.return_value = True
        arg4 = MagicMock()
        arg5 = MagicMock()
        rel14 = MagicMock()
        rel14.relfrom = arg1
        rel14.relto   = arg4
        rel52 = MagicMock()
        rel52.relfrom = arg5
        rel52.relto   = arg2
        rel54 = MagicMock()
        rel54.relfrom = arg5
        rel54.relto   = arg4

        extension = Extension(arg1, arg4)
        self.assertFalse(extension.is_admissible([rel14]))

        extension = Extension(arg1, arg2, arg3)
        self.assertTrue(extension.is_admissible([rel14]))

        arg2.is_acceptable.return_value = False
        self.assertFalse(extension.is_admissible([rel14, rel52, rel54]))

    def test_is_complete(self):
        arg1 = MagicMock()
        arg1.is_acceptable.return_value = True
        arg2 = MagicMock()
        arg2.is_acceptable.return_value = True
        arg3 = MagicMock()
        arg3.is_acceptable.return_value = True
        arg4 = MagicMock()
        arg4.is_acceptable.return_value = False

        extension = Extension(arg1, arg2, arg3)
        self.assertTrue(extension.is_complete([arg1, arg2, arg3, arg4], []))

        arg4.is_acceptable.return_value = True
        self.assertFalse(extension.is_complete([arg1, arg2, arg3, arg4], []))

    def test_is_stable(self):
        arg1 = MagicMock()
        arg2 = MagicMock()
        arg3 = MagicMock()
        arg4 = MagicMock()
        rel = MagicMock()
        rel.relfrom = arg1
        rel.relto = arg4

        extension = Extension(arg1, arg2, arg3)
        self.assertTrue(extension.is_stable([arg1, arg2, arg3, arg4], [rel]))

        arg5 = MagicMock()
        self.assertFalse(extension.is_stable([arg1, arg2, arg3, arg4, arg5], [rel]))
        rel2 = MagicMock()
        rel2.relfrom = arg1
        rel2.relto = arg2
        self.assertFalse(extension.is_stable([arg1, arg2, arg3, arg4], [rel, rel2]))

        rel3 = MagicMock()
        rel3.relfrom = arg4
        rel3.relto = arg1
        self.assertTrue(extension.is_stable([arg1, arg2, arg3, arg4], [rel, rel3]))
