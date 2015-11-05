from enum import Enum
from collections import defaultdict
from random import random

from . import Relation, RelationType


class FallacyType(Enum):
    BeggingTheQuestion         = 1
    IrrelevantConclusion       = 2
    FallacyOfIrrelevantPurpose = 3
    FallacyOfRedHerring        = 4
    ArgumentAgainstTheMan      = 5
    PoisoningTheWell           = 6
    FallacyOfTheBeard          = 7
    FallacyOfSlipperySlope     = 8
    FallacyOfFalseCause        = 9
    FallacyOfPreviousThis      = 10
    JointEffect                = 11
    WrongDirection             = 12
    FalseAnalogy               = 13
    SlothfulInduction          = 14
    AppealToBelief             = 15
    PragmaticFallacy           = 16
    FallacyOfIsToOught         = 17
    ArgumentFromForce          = 18
    ArgumentToPity             = 19
    PrejudicialLanguage        = 20
    FallacyOfSpecialPleading   = 21
    AppealToAuthority          = 22

class Premise:
    def __init__(self, id, text="", sources=None, probability=1):
        self.id        = id
        self.relations = list()
        self.text      = text
        self.sources   = sources or list()
        self.fallacies = defaultdict(int)
        self.probability = probability

    def add_relations(self, *relations):
        self.relations += [Relation(self, par, reltype) for par, reltype in relations]

    def supports(self):
        return [r.relto for r in self.relations if r.type == RelationType.support]

    def objects(self):
        return [r.relto for r in self.relations if r.type == RelationType.objection]

    def add_fallacies(self, *fallacies):
        for f in fallacies:
            self.fallacies[f] += 1

    def fallacies_count(self):
        return sum(self.fallacies.values())

    def is_acceptable(self, extension, relations):
        attacking = [rel.relfrom for rel in relations if rel.relto == self]
        if not attacking:
            return True
        for arg in attacking:
            if not any(rel for rel in relations if rel.relto == arg and rel.relfrom in extension.arguments):
                return False
        return True

    def is_present(self):
        return random() < self.probability

    def __str__(self):
        return str(id)

