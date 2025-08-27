# conftest.py
import pytest
from playwright.sync_api import sync_playwright
from screenplay.actor import Actor
from screenplay.abilities.browse_the_web import BrowseTheWeb

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()

@pytest.fixture(scope="session")
def app_url():
    return "file:///C:/Users/User/Documents/New_Screening_System.html"

@pytest.fixture
def user(page, app_url):
    return Actor("Usuario").can(BrowseTheWeb(page, app_url))
