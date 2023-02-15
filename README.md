README.md
Introduction
This project is an automated test using pytest, pycharm, and selenium webdriver to test the login functionality of a website.

Prerequisites
Python 3.x
Pytest
Pycharm
Selenium Webdriver
Chrome Driver
Conf file that contains the base URL of the website being tested
Environmental variables for the username and password
How to run the tests
Clone the repository to your local machine
Install the required packages using pip install -r requirements.txt
Set the environmental variables for the username and password
Open the project in Pycharm
Right-click on the test_case.py file and select Run
Test Description
The project contains two test cases:

test_login_page: This test case validates the different elements present on the login page such as the email field, password field, remember me checkbox, need help link, login with organization link, and sign-up link.

test_login: This test case performs the following actions:

Verifies that the session is logged out
Logs in to the website using the username and password provided through environmental variables
Verifies that the user is taken to the home page
Verifies that the user is logged in securely
Navigates using browser forward and back buttons to non-secure site, then back to secure site
Verifies that the user is still logged in
Verifies the user details by mouse over the user name
Logs out from the website
Verifies that the session is logged out
Error handling and Screenshots
In case of any test failure, a screenshot of the failure is captured and stored in the project directory with the file name format test_case_test_login_page_test_login.png.

Conclusion
This project provides a basic automated test for the login functionality of a website using pytest, pycharm, and selenium webdriver. The test cases validate the different elements on the login page and the login functionality of the website. In case of any test failure, the screenshot of the failure is captured for easy debugging.