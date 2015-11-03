from . import Relation


class Extension:
    def __init__(self, *arguments):
        self.arguments = arguments

    def add_arguments(self, *arguments):
        self.arguments += arguments

    def is_conflicting(self, relations):
        return any(rel for rel in relations if rel.relfrom in self.arguments and rel.relto in self.arguments)

    def is_conflict_free(self, relations):
        return not self.is_conflicting(relations)

    def is_admissible(self, relations):
        if not self.is_conflict_free(relations):
            return False
        return not any(arg for arg in self.arguments if not arg.is_acceptable(self, relations))

    def __str__(self):
        return ', '.join(str(arg) for arg in self.arguments)