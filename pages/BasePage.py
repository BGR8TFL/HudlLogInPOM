import locators
from config.conf import base_url

# This method will initialize the driver, URL, and locators.
class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = base_url
        self.locator = locators

    def navigate(self):
        self.driver.get(self.base_url)

    # This method will find an element on the page using the specified locator.
    def find_element(self, locator_type, locator):
        if locator_type == 'css':
            return self.driver.find_element_by_css_selector(locator)
        elif locator_type == 'xpath':
            return self.driver.find_element_by_xpath(locator)
        elif locator_type == 'id':
            return self.driver.find_element_by_id(locator)

    # This method will click an element on the page using the specified locator.
    def click_element(self, locator_type, locator):
        element = self.find_element(locator_type, locator)
        element.click()

    # This method will send keys to an element on the page using the specified locator.
    def send_keys(self, locator_type, locator, keys):
        element = self.find_element(locator_type, locator)
        element.send_keys(keys)

    # This method will return the title of the current page.
    def get_page_title(self):
        return self.driver.title

    # This method will navigate to the specified URL.
    def navigate_to(self):
        self.driver.get(self.base_url)
