"""
conftest.py: configuration settings and fixtures.

This module defines fixtures which can be used by test cases setting up the
environment. Also has configuration settings.

Fixtures:
    - setup_driver: creates a new instance Chrome WebDriver instance and returns it.
    - wait: returns WebDriverWait object with 10 sec timeout.
"""


import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="function")
def setup_driver():
    setup_driver = webdriver.Chrome()
    # setup_driver.set_window_position(-2000, 0)
    setup_driver.maximize_window()
    yield setup_driver
    setup_driver.quit()

@pytest.fixture(scope="function")
def wait(setup_driver):
    return WebDriverWait(setup_driver, timeout=10)