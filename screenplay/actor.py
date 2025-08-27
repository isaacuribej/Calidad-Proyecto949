class Actor:
    def __init__(self, name: str):
        self.name = name
        self.abilities = {}

    def can(self, ability: object):
        self.abilities[type(ability)] = ability
        return self

    def ability_to(self, ability_type: type):
        return self.abilities[ability_type]

    def attempts_to(self, *tasks):
        for task in tasks:
            task.perform_as(self)