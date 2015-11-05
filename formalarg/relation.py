from enum import Enum
from random import random


class RelationType(Enum):
    objection = 0
    support   = 1
    situation = 2


class Relation:
    def __init__(self, relfrom, relto, type=RelationType.situation, probability=1):
        self.type        = type
        self.relfrom     = relfrom
        self.relto       = relto
        self.supporters  = 0
        self.opponents   = 0
        self.probability = 1

    def add_supporters(self, count):
        self.supporters += count

    def add_opponents(self, count):
        self.opponents += count

    def support_difference(self):
        return self.supporters - self.opponents

    def is_present(self):
        if self.relfrom.is_present() and self.relto.is_present():
            return random() < self.probability
        return False
