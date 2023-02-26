from selene import browser
import pytest


@pytest.fixture(scope='session')
def browser_configs():
    browser.config.window_width = 720
    browser.config.window_height = 900
    browser.open('https://www.google.com/')
