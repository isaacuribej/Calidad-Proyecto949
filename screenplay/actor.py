# screenplay/actor.py

from dataclasses import dataclass, field

class Task:
    def perform_as(self, actor):
        raise NotImplementedError

@dataclass
class Actor:
    name: str
    abilities: dict = field(default_factory=dict)

    def can(self, ability):
        self.abilities[type(ability)] = ability
        return self

    def ability_to(self, ability_cls):
        return self.abilities[ability_cls]

    def attempts_to(self, *tasks: Task):
        for t in tasks:
            t.perform_as(self)
        return self
