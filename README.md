# Readme

[![](https://img.shields.io/badge/hudl-OSS-orange.svg)](http://hudl.github.io/)

This project is a Python-based framework using the Page Object Model (POM) approach built with pytest and Selenium WebDriver for logging into the Hudl web application. It includes test cases that validate login functionality and user experience.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Files](#files)
- [Test Artifacts](#test-artifacts)
- [Creator](#creator)

## Prerequisites
- Python 3.x
- Pytest
- Pycharm (or other IDE)
- Selenium Webdriver
- Chrome Driver
- Conf file that contains the base URL of the website being tested, included in repo.
- Environmental variables for `HUDL_EMAIL` and `HUDL_PASSWORD`


## Getting Started
To get started with this project, you will need Python 3 and PyCharm installed on your machine.

1. Clone this repository to your local machine.
2. Open the HudlLogInPOM directory in PyCharm.
3. Install the required Python packages by running the following command in the terminal: `pip install -r requirements.txt`
4. Set up the environment variables for the `HUDL_EMAIL` and `HUDL_PASSWORD` in your operating system or in PyCharm.
5. Run the tests by selecting the test case in PyCharm and clicking the "Run" button, or Right-click on the test_case.py file and select Run.


## Usage
This POM framework includes two test cases for the Hudl login page:

1. `test_login_page`: This test case validates the presence of the email, password, remember me checkbox, need help link, log in with an organization link, and sign up link fields on the login page.
2. `test_login`: This test case validates the login functionality by logging in with the provided credentials, checking for secure login, verifying the user is logged in as the correct user, verifying the user is able to log out successfully, and checking that the user is redirected to the login page after logging out.
3. `test_login_with_incorrect_credentials`: Test case verifies login page displays error message with incorrect credentials.


## Files
This project includes the following files:

- `test_case.py`: This file contains the two test cases for the Hudl login page.
- `conftest.py`: This file contains configuration settings for the project.
- `conf.py`: This file contains configuration settings for the project, including the base URL and browser type.
- `utils.py`: This file contains a function for waiting for an expected condition to be met within a specified timeout.
- `locators.py`: This file contains the element locators used in the test cases.
- `LoginPage.py`: This file contains the specific functions and elements that are unique to the login page in the web application.
- `BasePage.py`: This file contains the base class for the Page Object Model framework, including the driver, URL, and locators.
- `test_artifacts.pdf`:  This file contains the Test Plan, Test Cases and phase 2 testing out of scope for this interview project.


## Test Artifacts
- Test Plan
- Test Cases
- Future testing Phase 2
- See [Test Artifacts](https://github.com/BGR8TFL/HudlLogInPOM/blob/main/test_artifacts.pdf)



## Creator
Contributions to this project are welcome! If you find a bug or would like to suggest an enhancement, please open an issue or submit a pull request.
