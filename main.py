import datetime
import json
from functions import *
import time
from datetime import datetime
from bs4 import BeautifulSoup # type: ignore
from selenium.webdriver.common.by import By # type: ignore
from selenium.webdriver.support.ui import WebDriverWait # type: ignore
from selenium.webdriver.common.action_chains import ActionChains # type: ignore
from selenium.webdriver.support.ui import Select


#%%
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

driver = get_url()
get_to_details_page(driver)
inputDetails(driver)
