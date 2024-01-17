import pytest
from selene import browser, have, be

@pytest.fixture()
def browser_setup():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield
    browser.quit()