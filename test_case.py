"""
test_case.py:

This module has test cases that are run using Page Object Model (POM) for the Hudl website login functionality. Test cases cover the following scenarios:

- Verification of login page.
- Prevent Login with incorrect credentials, display and validate error message.
- Successful login, access to the home page and other verifications ensuring correct user is logged in.

Tests designed to be run using PyTest and are dependent on "conf.py" file for configuration, "conftest.py" for settings and fixtures, "locators.py" file for locators and "pages" package for page functions.

Each test case has its own docstring outlining the scenario it covers and the expected behavior.

Author: [Jason Avery]
Date: [February 18, 2023]
"""


import os
from selenium.webdriver.common.action_chains import ActionChains
from locators import Locators
from pages.LoginPage import LoginPageClass
import conf
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException, StaleElementReferenceException, ElementNotInteractableException


def test_login_page(setup_driver, wait):
    """
    Test case verifies login page.

    Test case verifies login page displayed correctly and all necessary UI elements are present.

    Args:
        setup_driver: A WebDriver instance, initialized with appropriate browser and settings.
        wait: WebDriverWait instance to wait for elements on the page.

    Raises:
        Exceptions that occur during test execution.
    """
    # Initialize WebDriver
    driver = setup_driver
    wait = wait
    try:
        setup_driver.get(f"{conf.base_url}/login")
        login_page = LoginPageClass(setup_driver)

        # Validate page title
        assert setup_driver.title == "Log In"

        # Validate "Email" field
        email_field = driver.find_element(*Locators.EMAIL_FIELD)
        assert email_field.is_displayed()

        # Validate "Password" field
        password_field = driver.find_element(*Locators.PASSWORD_FIELD)
        assert password_field.is_displayed()

        # Validate "Remember me" check box
        remember_me_checkbox = driver.find_element(*Locators.REMEMBER_ME_CHECKBOX)
        assert remember_me_checkbox.is_displayed()

        # Validate "Need help?" link
        need_help_link = driver.find_element(*Locators.NEED_HELP_LINK)
        assert need_help_link.is_displayed()

        # Validate "Log In with an Organization" link
        login_with_org_link = driver.find_element(*Locators.LOG_IN_WITH_ORGANIZATION_LINK)
        assert login_with_org_link.is_displayed()

        # Validate "Sign up" link
        sign_up_link = driver.find_element(*Locators.SIGN_UP_LINK)

        assert sign_up_link.is_displayed()
    except Exception as e:
        print(f"Error in the test_login_page: {e}")
        raise e

def test_login_with_incorrect_credentials(setup_driver, wait):
    """
    Test case verifies login page displays error message with incorrect credentials.

    Test case enters incorrect email and password then clicks Login button and then verifies correct error message is displayed.

    Args:
        setup_driver: A WebDriver instance, initialized with appropriate browser and settings.
        wait: WebDriverWait instance to wait for elements on the page.

    Raises:
        Exceptions that occur during test execution.
    """
    # Initialize WebDriver
    driver = setup_driver
    wait = wait
    try:
        setup_driver.get(f"{conf.base_url}/login")
        login_page = LoginPageClass(setup_driver)

        # Enter incorrect email and password
        login_page.enter_incorrect_email("incorrect_email@incorrect_email.com")
        login_page.enter_incorrect_password("incorrect_password")

        # Click Login button
        login_page.click_login(*Locators.LOGIN_BUTTON)

        # Verify error message is displayed
        error_message = wait.until(EC.presence_of_element_located(Locators.ERROR_DISPLAY))
        is_error_message_displayed = error_message.is_displayed()

    except Exception as e:
        print(f"Error in the test_login_with_incorrect_credentials: {e}")
        raise e


def test_login(setup_driver, wait):
    """
    Test verifies user can log in and access the home page.

    Test case enters incorrect email and password then clicks Login button, then verifies user is taken to home page. Also validates additional checks verifying user is logged in correctly.

    Args:
        setup_driver: A WebDriver instance, initialized with appropriate browser and settings.
        wait: WebDriverWait instance to wait for elements on the page.

    Raises:
        Exceptions that occur during test execution.
    """
    # Initialize WebDriver
    driver = setup_driver
    wait = wait
    try:
        # Initialize WebDriver
        # Verify session is logged out
        setup_driver.get(f"{conf.base_url}/logout")

        # Go to login page
        setup_driver.get(f"{conf.base_url}/login")
        login_page = LoginPageClass(setup_driver)

        # Enter email and password
        login_page.enter_email(os.environ["HUDL_EMAIL"])
        login_page.enter_password(os.environ["HUDL_PASSWORD"])

        # Click Login button
        login_page.click_login(*Locators.LOGIN_BUTTON)

        # Verify user is taken to the base URL page by verifying the title
        wait.until(EC.url_to_be("https://www.hudl.com/home"))
        assert setup_driver.title == "Home - Hudl"

        # Verify user is taken to the home page
        assert setup_driver.current_url == "https://www.hudl.com/home"

        # Check if user is logged in securely
        assert setup_driver.current_url.startswith("https://")

        # Navigate using browser forward and back buttons to non-secure site, then back to secure hudl https://www.hudl.com/home
        setup_driver.get("http://www.weather.com/")
        assert setup_driver.current_url == "https://weather.com/"
        setup_driver.back()
        assert setup_driver.current_url == "https://www.hudl.com/home"

        # Verify that the user is taken to the home page
        setup_driver.get(f"{conf.base_url}/home")
        wait.until(EC.url_to_be("https://www.hudl.com/home"))
        assert setup_driver.current_url == "https://www.hudl.com/home"

        # Verify that the user is still logged in
        user_name = driver.find_element(*Locators.USER_PROFILE_NAME)
        assert user_name.text == "Jason Avery"

        # Verify the user you just logged in as "Jason Avery" text is visible
        assert user_name.is_displayed()

        # Mouse over user "Jason Avery"
        actions = ActionChains(setup_driver)
        actions.move_to_element(user_name).perform()

        # When the dropdown menu expands, verify "averyjl@gmail.com" is present
        email = driver.find_element(*Locators.EMAIL_IN_DROPDOWN)
        assert email.text == "averyjl@gmail.com"
        assert email.is_displayed()

        # Select "Log Out"
        logout = driver.find_element(*Locators.LOGOUT_LINK)
        logout.click()

        # Verify that the user is taken to the base URL page by verifying the title
        assert setup_driver.title == "Hudl • Tools to help every team, coach and athlete improve"

        # Verify that the session is logged out - expecting "https://www.hudl.com/login?forward=%2Fhome" - URL redirecting
        ## to the login page with the forward parameter set to %2Fhome (typically used to track the page you were trying
        ## to access before being redirected to the login page. When you are logged in, the website can redirect
        ## back to the page specified by the forward parameter.)

        setup_driver.get(f"{conf.base_url}/home")
        assert setup_driver.current_url == "https://www.hudl.com/login?forward=%2Fhome"

    # Exception Handling
    # Timeout Exception
    except TimeoutException as te:
        print(f"Error: TimeoutException occurred while waiting for page to load. {te}")
        raise te
    # StaleElementReference Exception
    except StaleElementReferenceException as sere:
        print(f"Error: StaleElementReferenceException occurred a reference to an element became stale. {sere}")
        raise sere
    # NoSuchElement Exception
    except NoSuchElementException as nse:
        print(f"Error: NoSuchElementException occurred an element could not be found. {nse}")
        raise nse
    # WebDriver Exception
    except WebDriverException as wde:
        print(f"Error: WebDriverException occurred with the underlying WebDriver implementation. {wde}")
        raise wde
    # AssertionError Exception
    except AssertionError as ae:
        print(f"Assertion error occurred: {ae}")
        raise ae
    # Exception
    except Exception as e:
        print(f"General Exception: {e}")
        raise e


def pytest_assertion_interact(node, report):
    """
    Helper function to take a screenshot when an assertion fails.

    This function is used by PyTest to take a screenshot of the browser when an assertion fails. The screenshot is saved to a file that includes the name of the test case that failed.

    Args:
        node: The PyTest test node that failed.
        report: The PyTest report for the test that failed.

    Raises:
        Any exceptions that occur during screenshot capture will be ignored.
    """
    if report.when == "call" and report.failed:
        file_name = f"{node.parent.parent.name}_{node.parent.name}_{node.name}.png"
        node.parent.parent.parent.driver.get_screenshot_as_file(file_name)