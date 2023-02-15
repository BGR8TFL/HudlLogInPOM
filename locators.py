# locators.py:  contains element locators used in the test cases.

from selenium.webdriver.common.by import By

# Login page locators
class LoginPageLocators:
    LOGIN_LINK = (By.LINK_TEXT, 'Log In')
    LOGIN_PAGE_TITLE = (By.XPATH, '//h1[text()="Log In"]')
    EMAIL_FIELD = (By.ID, 'email')
    PASSWORD_FIELD = (By.ID, 'password')
    REMEMBER_ME_CHECKBOX = (By.CSS_SELECTOR, 'input[type="checkbox"]')
    NEED_HELP_LINK = (By.LINK_TEXT, 'Need help?')
    LOG_IN_WITH_ORGANIZATION_LINK = (By.LINK_TEXT, 'Log In with an Organization')
    SIGN_UP_LINK = (By.LINK_TEXT, 'Sign up')
    LOGIN_BUTTON = (By.ID, 'logIn')

    # Home page locators
class HomePageLocators:
    HOME_PAGE_TITLE = (By.XPATH, '//h1[text()="Home"]')
    SECURE_LOGIN_MESSAGE = (By.XPATH, '//div[text()="You are logged in securely"]')
    USER_PROFILE_DROPDOWN = (By.CSS_SELECTOR, 'span.dropdown-toggle')
    USER_PROFILE_NAME = (By.CSS_SELECTOR, 'span.username')
    EMAIL_IN_DROPDOWN = (By.XPATH, '//a[text()="averyjl@gmail.com"]')
    LOGOUT_LINK = (By.XPATH, '//a[text()="Log Out"]')
