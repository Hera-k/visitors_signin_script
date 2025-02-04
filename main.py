#%%
from functions import create_driver
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

#%%
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()


#%%
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
driver = create_driver(user_agent)
# %%
url = "https://fg-nexus.co.za/"
driver.get(url)
wait = WebDriverWait(driver,10)

#%%
to_click = "#app > div > main > div > div:nth-child(2) > div"
element = driver.find_element(By.CSS_SELECTOR, to_click)
driver.execute_script("arguments[0].click();", element)

# %%
# Access them
email_address = os.getenv("email_address")
email_address_element =  driver.find_element(By.XPATH, ("//*[@id='email']"))
email_address_element.send_keys(email_address)
# %%
password = os.getenv("password")
password_element = driver.find_element(By.XPATH, ("//*[@id='password']"))
password_element.send_keys(password)
#%%
login_button_element = "#app > div > main > div.relative > div.fixed.inset-x-8.sm\:inset-x-8.top-28.sm\:top-28.bottom-28.sm\:bottom-28.mx-auto.max-w-lg.bg-white.rounded-lg.shadow-lg.z-30.max-h-\[90vh\].overflow-y-auto > div > form > div > button > span"
login_button_click = driver.find_element(By.CSS_SELECTOR, login_button_element)
driver.execute_script("arguments[0].click();", login_button_click)
time.sleep(20)

# %%
visitors_button = "#app > div > div > main > section > main > div > a:nth-child(14)"
visitors_element = driver.find_element(By.CSS_SELECTOR, visitors_button)
driver.execute_script("arguments[0].click();", visitors_element)
time.sleep(20)
# %%
book_a_stay = "#app > div > div > main > section > main > div > a"
book_a_stay_element = driver.find_element(By.CSS_SELECTOR, book_a_stay)
driver.execute_script("arguments[0].click();", book_a_stay_element)
time.sleep(1000)