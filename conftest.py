import pytest
from selene import browser


@pytest.fixture(scope='function')
def browser_set():
    browser.config.window_width = 800
    browser.config.window_height = 600
    yield
    browser.quit()
