# LoginPage.py:  contains the specific functions and elements that are unique to the login page in the web application.

import os
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.email_textbox = (By.ID, "email")
        self.password_textbox = (By.ID, "password")
        self.remember_me_checkbox = (By.ID, "rememberMe")
        self.login_button = (By.ID, "logIn")

    def get_email_field(self):
        return self.driver.find_element(By.ID, "email")

    def get_password_field(self):
        return self.driver.find_element(By.ID, "password")

    def get_remember_me_checkbox(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'input[type="checkbox"]')

    def get_need_help_link(self):
        return self.driver.find_element(By.LINK_TEXT, 'Need help?')

    def get_login_with_org_link(self):
        return self.driver.find_element(By.LINK_TEXT, 'Log In with an Organization')

    def get_sign_up_link(self):
        return self.driver.find_element(By.LINK_TEXT, 'Sign up')

    def enter_email(self, email):
        self.fill_form_element_email(self.email_textbox, email)

    def enter_password(self, password):
        self.fill_form_element_password(self.password_textbox, password)

    def check_remember_me(self):
        self.find_element(self.remember_me_checkbox, "rememberMe").click()

    def click_login(self, by, locator):
        self.driver.find_element(by, locator).click()


    def fill_form_element_email(self, email_textbox, email):
        self.driver.find_element(By.ID, "email").send_keys(os.environ["HUDL_EMAIL"])

    def fill_form_element_password(self, password_textbox, password):
        self.driver.find_element(By.ID, "password").send_keys(os.environ["HUDL_PASSWORD"])

    def get_title(self):
        return self.driver.title

    def is_email_field_present(self):
        email_field = self.driver.find_element_by_id("email")
        if email_field:
            return True
        else:
            return False

    def is_password_field_present(self):
        password_field = self.driver.find_element_by_id("password")
        if password_field:
            return True
        else:
            return False

    def is_remember_me_checkbox_present(self):
        remember_me_checkbox = self.driver.find_element_by_id("rememberMe")
        if remember_me_checkbox:
            return True
        else:
            return False

    def is_need_help_link_present(self):
        need_help_link = self.driver.find_element_by_link_text("Need help?")
        if need_help_link:
            return True
        else:
            return False

    def is_login_with_org_link_present(self):
        login_with_org_link = self.driver.find_element_by_link_text("Login with Org")
        if login_with_org_link:
            return True
        else:
            return False

    def is_sign_up_link_present(self):
        sign_up_link = self.driver.find_element_by_link_text("Sign Up")
        if sign_up_link:
            return True
        else:
            return False

    def click_login_button(self):
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

    def is_logged_in_as_text_present(self, name):
        try:
            element = self.driver.find_element(By.XPATH, "//p[contains(text(), 'Logged in as') and contains(text(), name)]")
            return element.is_displayed()
        except NoSuchElementException:
            return False

    def mouse_over_user(self):
        user_element = self.driver.find_element(By.XPATH, "//span[@class='user-name']")
        actions = ActionChains(self.driver)
        actions.move_to_element(user_element).perform()

###    # The dropdown selector and email elements selector should be replaced with the actual selectors for the dropdown and the email elements respectively.
    def is_email_present_in_dropdown(self, email):
        dropdown_element = self.driver.find_element(By.CSS_SELECTOR, "dropdown selector")
        email_elements = dropdown_element.find_elements(By.CSS_SELECTOR, "email elements selector")
        for element in email_elements:
            if element.text == email:
                return True
        return False

    def click_log_out(self):
        # locate the logout button on the page and click it
        log_out_button = self.driver.find_element(By.XPATH, "//a[text()='Log Out']")
        log_out_button.click()














