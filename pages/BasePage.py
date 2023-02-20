"""
BasePage.py:

This module has BasePageClass, which provides functions for interacting with web pages like clicking links and filling out fields.

Attributes:
    - driver: instance of Selenium WebDriver used for browser automation.
    - base_url: base URL of web app being tested.
    - locators: module with element locators for the test cases.

Methods:
    - __init__(self, driver): initializes driver, URL and locators.
    - navigate(self): navigates to base URL of app being tested.
    - find_element(self, locator_type, locator): finds element using specified locator.
    - click_element(self, locator_type, locator): clicks element on page using locator.
    - send_keys(self, locator_type, locator, keys): sends keys to element on page using locator.
    - get_page_title(self): returns title of current page.
    - navigate_to(self): navigates to base URL of appl.
"""


import locators
from conf import base_url


# This method initializes driver, URL, and locators.
class BasePageClass:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = base_url
        self.locator = locators

    def navigate(self):
        self.driver.get(self.base_url)

    # This method finds element on page using specified locator.
    def find_element(self, locator_type, locator):
        if locator_type == 'css':
            return self.driver.find_element_by_css_selector(locator)
        elif locator_type == 'xpath':
            return self.driver.find_element_by_xpath(locator)
        elif locator_type == 'id':
            return self.driver.find_element_by_id(locator)

    # This method clicks element on page using specified locator.
    def click_element(self, locator_type, locator):
        element = self.find_element(locator_type, locator)
        element.click()

    # This method sends keys to element on page using specified locator.
    def send_keys(self, locator_type, locator, keys):
        element = self.find_element(locator_type, locator)
        element.send_keys(keys)

    # This method returns title of current page.
    def get_page_title(self):
        return self.driver.title

    # This method navigates to specified URL.
    def navigate_to(self):
        self.driver.get(self.base_url)