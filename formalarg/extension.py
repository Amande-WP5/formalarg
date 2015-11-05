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

    def is_complete(self, arguments, relations):
        if not self.is_admissible(relations):
            return False
        for arg in arguments:
            if arg.is_acceptable(self, relations) and not arg in self.arguments:
                return False
        return True

    def is_stable(self, arguments, relations):
        if not self.is_conflict_free(relations):
            return False
        arg_not_in_ext = [arg for arg in arguments if not arg in self.arguments]
        atked = [rel.relto for rel in relations if rel.relfrom in self.arguments and rel.relto in arg_not_in_ext]
        return not any(arg for arg in arg_not_in_ext if arg not in atked)

    def __str__(self):
        return ', '.join(str(arg) for arg in self.arguments)