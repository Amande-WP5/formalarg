class Graph:
    def __init__(self):
        self.arguments = list()
        self.relations = list()

    def add_arguments(self, *arguments):
        self.arguments += arguments

    def add_relations(self, *relations):
        self.relations += relations
