import graphviz as gv

from . import RelationType

def type_to_color(type):
    if type == RelationType.objection:
        return 'red'
    elif type == RelationType.support:
        return 'green'
    return 'yellow'

class Graph:
    def __init__(self):
        self.arguments = list()
        self.relations = list()

    def add_arguments(self, *arguments):
        self.arguments += arguments

    def add_relations(self, *relations):
        self.relations += relations

    def draw(self, form, filename):
        graph = gv.Digraph(format=form)
        for arg in self.arguments:
            graph.node(str(arg.id))

        for rel in self.relations:
            graph.edge(str(rel.relfrom.id), str(rel.relto.id), color=type_to_color(rel.type))
        graph.render(filename=filename)
