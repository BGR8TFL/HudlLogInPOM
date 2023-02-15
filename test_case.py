# test_case.py:  contains the actual test cases that are run using the Page Object Model.

import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from pages.LoginPage import LoginPage
from config import conf


@pytest.fixture(scope="module")
def setup_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    # driver.set_window_position(-2000, 0)

    yield driver
    driver.quit()

def test_login_page(setup_driver):
    try:
        driver = setup_driver
        driver.get(f"{conf.base_url}/login")
        login_page = LoginPage(driver)

        # Validate page title
        assert driver.title == "Log In"

        # Validate "Email" field
        email_field = login_page.get_email_field()
        assert email_field.is_displayed()

        # Validate "Password" field
        password_field = login_page.get_password_field()
        assert password_field.is_displayed()

        # Validate "Remember me" check box
        remember_me_checkbox = login_page.get_remember_me_checkbox()
        assert remember_me_checkbox.is_displayed()

        # Validate "Need help?" link
        need_help_link = login_page.get_need_help_link()
        assert need_help_link.is_displayed()

        # Validate "Log In with an Organization" link
        login_with_org_link = login_page.get_login_with_org_link()
        assert login_with_org_link.is_displayed()

        # Validate "Sign up" link
        sign_up_link = login_page.get_sign_up_link()
        assert sign_up_link.is_displayed()
    except Exception as e:
        print(f"Error: {e}")
        raise e

def test_login(setup_driver):
    try:
        driver = setup_driver

        # Verify that the session is logged out
        driver.get(f"{conf.base_url}/logout")

        driver.get(f"{conf.base_url}/login")
        login_page = LoginPage(driver)

        # Enter email and password
        login_page.enter_email(os.environ["HUDL_EMAIL"])
        login_page.enter_password(os.environ["HUDL_PASSWORD"])

        # Click Login button
        login_page.click_login(By.ID, "logIn")
        time.sleep(5)

        # Verify that the user is taken to the base URL page by verifying the title
        assert driver.title == "Home - Hudl"

        # Verify that the user is taken to the home page
        assert driver.current_url == "https://www.hudl.com/home"

        # Check if the user is logged in securely
        assert driver.current_url.startswith("https://")

        # Navigate using browser forward and back buttons to non-secure site, then back to secure hudl https://www.hudl.com/home
        driver.get("http://www.weather.com/")
        time.sleep(2)
        driver.back()

        # Verify that the user is taken to the home page
        driver.get(f"{conf.base_url}/home")
        time.sleep(2)
        assert driver.current_url == "https://www.hudl.com/home"

        # Verify that the user is still logged in
        time.sleep(5)
        user_name = driver.find_element(By.CSS_SELECTOR, ".hui-globaluseritem__display-name > span")
        assert user_name.text == "Jason Avery"

        # Verify the user you just logged in as "Jason Avery" text is visible
        assert user_name.is_displayed()

        # Mouse over user "Jason Avery"
        # #Action
        actions = ActionChains(driver)
        actions.move_to_element(user_name).perform()

        # When the dropdown menu expands, verify "averyjl@gmail.com" is present
        email = driver.find_element(By.CSS_SELECTOR, ".hui-globaluseritem__email")
        assert email.text == "averyjl@gmail.com"
        assert email.is_displayed()

        # Select "Log Out"
        logout = driver.find_element(By.LINK_TEXT, "Log Out")
        logout.click()

        # Verify that the user is taken to the base URL page by verifying the title
        assert driver.title == "Hudl • Tools to help every team, coach and athlete improve"

        # Verify that the session is logged out - expecting "https://www.hudl.com/login?forward=%2Fhome" - URL redirecting
        ## to the login page with the forward parameter set to %2Fhome (typically used to track the page you were trying
        ## to access before being redirected to the login page. When you are logged in, the website can redirect
        ## back to the page specified by the forward parameter.)

        driver.get(f"{conf.base_url}/home")
        assert driver.current_url == "https://www.hudl.com/login?forward=%2Fhome"
    except Exception as e:
        print(f"Error: {e}")
        raise e

    # Add code to capture screenshots in case of test failure
def pytest_assertion_interact(node, report):
    if report.when == "call" and report.failed:
        file_name = f"{node.parent.parent.name}_{node.parent.name}_{node.name}.png"
        node.parent.parent.parent.driver.get_screenshot_as_file(file_name)
