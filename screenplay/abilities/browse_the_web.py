# screenplay/abilities/browse_the_web.py

from playwright.sync_api import Page

class BrowseTheWeb:
    def __init__(self, page, base_url: str):
        self.page = page
        self.base_url = base_url

    @staticmethod
    def using(page, base_url: str):
        return BrowseTheWeb(page, base_url)

    def get_page(self):
        return self.page