#conf.py: contains configuration settings for the project.

import os

# Configuration settings for the test environment
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
