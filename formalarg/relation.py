from enum import Enum


class RelationType(Enum):
    objection = 0
    support   = 1
    situation = 2


class Relation:
    def __init__(self, relfrom, relto, type):
        self.type       = type
        self.relfrom    = relfrom
        self.relto      = relto
        self.supporters = 0
        self.opponents  = 0

    def add_supporters(self, count):
        self.supporters += count

    def add_opponents(self, count):
        self.opponents += count

    def support_difference(self):
        return self.supporters - self.opponents
