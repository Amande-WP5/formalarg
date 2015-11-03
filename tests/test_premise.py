import unittest
from unittest.mock import MagicMock

from formalarg import Premise, Relation, RelationType, FallacyType


class TestPremise(unittest.TestCase):
    @unittest.skip("Not implemented")
    def test_init(self):
        self.fail("Not Implemented")

    @unittest.skip("Not implemented")
    def test_add_relations(self):
        self.fail("Not Implemented")

    def test_supports_without_parents(self):
        premise = Premise(1)

        self.assertEqual(premise.supports(), [])

    def test_supports_with_parents_without_supports(self):
        premise   = Premise(1)
        rel1      = MagicMock()
        rel2      = MagicMock()
        rel1.type = RelationType.objection
        rel2.type = RelationType.situation
        premise.relations = [rel1, rel2]

        self.assertEqual(premise.supports(), [])

    def test_supports_with_parents(self):
        premise   = Premise(1)
        rel       = MagicMock()
        rel.type  = RelationType.support
        premise.relations = [rel]

        self.assertEqual(len(premise.supports()), 1)

    def test_objections_without_parents(self):
        premise = Premise(1)

        self.assertEqual(premise.objects(), [])

    def test_objections_with_parents_without_objections(self):
        premise   = Premise(1)
        rel1      = MagicMock()
        rel2      = MagicMock()
        rel1.type = RelationType.support
        rel2.type = RelationType.situation
        premise.relations = [rel1, rel2]

        self.assertEqual(premise.objects(), [])

    def test_objections_with_parents(self):
        premise   = Premise(1)
        rel       = MagicMock()
        rel.type  = RelationType.objection
        premise.relations = [rel]

        self.assertEqual(len(premise.objects()), 1)

    def test_add_fallacies_and_count_without_fallacies(self):
        premise = Premise(1)

        self.assertEqual(len(premise.fallacies), 0)
        self.assertEqual(premise.fallacies_count(), 0)

    def test_add_fallacies_and_count_with_0_fallacies(self):
        premise = Premise(1)
        premise.add_fallacies()

        self.assertEqual(len(premise.fallacies), 0)
        self.assertEqual(premise.fallacies_count(), 0)

    def test_add_fallacies_and_count_with_1_fallacy(self):
        premise = Premise(1)
        premise.add_fallacies(FallacyType.BeggingTheQuestion)

        self.assertEqual(len(premise.fallacies), 1)
        self.assertEqual(premise.fallacies_count(), 1)
        self.assertEqual(premise.fallacies[FallacyType.BeggingTheQuestion], 1)

    def test_add_fallacies_and_count_with_more_fallacies(self):
        premise = Premise(1)
        premise.add_fallacies(FallacyType.BeggingTheQuestion, FallacyType.FallacyOfTheBeard, FallacyType.BeggingTheQuestion)

        self.assertEqual(len(premise.fallacies), 2)
        self.assertEqual(premise.fallacies_count(), 3)
        self.assertEqual(premise.fallacies[FallacyType.BeggingTheQuestion], 2)

    def test_is_acceptable(self):
        premise = Premise(1)
        arg1    = MagicMock()
        arg2    = MagicMock()
        arg3    = MagicMock()

        rel         = MagicMock()
        rel.relfrom = arg1
        rel.relto   = premise

        extension = MagicMock()
        extension.arguments = [arg2]
        self.assertTrue(premise.is_acceptable(extension, []))
        self.assertFalse(premise.is_acceptable(extension, [rel]))

        rel2         = MagicMock()
        rel2.relfrom = arg2
        rel2.relto   = arg1
        self.assertTrue(premise.is_acceptable(extension, [rel, rel2]))

        rel3         = MagicMock()
        rel3.relfrom = arg3
        rel3.relto   = arg1
        self.assertFalse(premise.is_acceptable(extension, [rel, rel3]))


if __name__ == '__main__':
    unittest.main()
