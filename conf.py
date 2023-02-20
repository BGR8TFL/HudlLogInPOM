"""
conf.py:

This module contains configuration settings.

Variables:
- base_url: str - base URL of the app.
- BROWSER: str - browser used.
- HUDL_EMAIL: str - email address used (not saved in project repo).
- HUDL_PASSWORD: str - password used (not saved in project repo).

If HUDL_EMAIL and HUDL_PASSWORD environment variables are set, their values are used for login. Otherwise, set to an empty string.
"""


import os


base_url = "https://www.hudl.com"
BROWSER = "Chrome"

# Check if the HUDL_EMAIL and HUDL_PASSWORD environment variables are set
# if yes, store values in respective variables. If environment variables not set, set the variables to an empty string.
# this allows us to keep the sensitive information such as emails and passwords in the test_env.env file and not in repo.
if "HUDL_EMAIL" in os.environ:
    HUDL_EMAIL = os.environ["HUDL_EMAIL"]
else:
    HUDL_EMAIL = ""

if "HUDL_PASSWORD" in os.environ:
    HUDL_PASSWORD = os.environ["HUDL_PASSWORD"]
else:
    HUDL_PASSWORD = ""