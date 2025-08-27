# screenplay/tasks/navigate_to.py

from screenplay.actor import Task
from screenplay.abilities.browse_the_web import BrowseTheWeb

class NavigateTo(Task):
    def __init__(self, url: str):
        self.url = url

    def perform_as(self, actor):
        page = actor.ability_to(BrowseTheWeb).page
        page.goto(self.url)
