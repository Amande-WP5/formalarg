import unittest
from unittest.mock import MagicMock

from formalarg import Graph, RelationType


class TestGraph(unittest.TestCase):
    def test_draw(self):
        graph = Graph()
        arg1 = MagicMock()
        arg1.id = "arg1"
        arg2 = MagicMock()
        arg2.id = "arg2"
        arg3 = MagicMock()
        arg3.id = "arg3"
        graph.add_arguments(arg1, arg2, arg3)

        rel1 = MagicMock()
        rel1.relfrom = arg1
        rel1.relto   = arg2
        rel1.type    = RelationType.support
        rel2 = MagicMock()
        rel2.relfrom = arg1
        rel2.relto   = arg3
        rel2.type    = RelationType.objection
        graph.add_relations(rel1, rel2)

        graph.draw('png', 'test')

