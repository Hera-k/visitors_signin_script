from selenium import webdriver
import undetected_chromedriver as uc
import datetime
import json
import time
from datetime import datetime
from bs4 import BeautifulSoup # type: ignore
from selenium.webdriver.common.by import By # type: ignore
from selenium.webdriver.support.ui import WebDriverWait # type: ignore
from selenium.webdriver.common.action_chains import ActionChains # type: ignore
from selenium.webdriver.support.ui import Select
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

def create_driver(user_agent):
    options = webdriver.ChromeOptions()
    options.add_argument(f'--user-agent={user_agent}')
    options.add_argument("--window-size=1920,1080")
    options.headless = False
    options.add_argument("--disable-blink-features=AutomationControlled")  # Avoid detection
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")

    driver = uc.Chrome(options=options, use_subprocess=True)

    return driver
def get_url():
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
    driver = create_driver(user_agent)
    url = "https://fg-nexus.co.za/"
    driver.get(url)
    wait = WebDriverWait(driver,5)
    return driver

def get_to_details_page(driver):
    
    to_click = "#app > div > main > div > div:nth-child(2) > div"
    element = driver.find_element(By.CSS_SELECTOR, to_click)
    driver.execute_script("arguments[0].click();", element)
    # Access them
    email_address = os.getenv("email_address")
    email_address_element =  driver.find_element(By.XPATH, ("//*[@id='email']"))
    email_address_element.send_keys(email_address)
    password = os.getenv("password")
    password_element = driver.find_element(By.XPATH, ("//*[@id='password']"))
    password_element.send_keys(password)
    time.sleep(5)
    login_button_element = "#app > div > main > div.relative > div.fixed.inset-x-8.sm\:inset-x-8.top-28.sm\:top-28.bottom-28.sm\:bottom-28.mx-auto.max-w-lg.bg-white.rounded-lg.shadow-lg.z-30.max-h-\[90vh\].overflow-y-auto > div > form > div > button > span"
    login_button_click = driver.find_element(By.CSS_SELECTOR, login_button_element)
    driver.execute_script("arguments[0].click();", login_button_click)
    time.sleep(5)
    visitors_button = "#app > div > div > main > section > main > div > a:nth-child(14)"
    visitors_element = driver.find_element(By.CSS_SELECTOR, visitors_button)
    driver.execute_script("arguments[0].click();", visitors_element)
    time.sleep(5)
    book_a_stay = "#app > div > div > main > section > main > div > a"
    book_a_stay_element = driver.find_element(By.CSS_SELECTOR, book_a_stay)
    driver.execute_script("arguments[0].click();", book_a_stay_element)
    time.sleep(5)

def inputDetails(driver):
    #%%
    type_of_visit_element = "#type_of_visit"
    type_of_visit_dropdown = Select(driver.find_element(By.CSS_SELECTOR, type_of_visit_element))
    #Select day visit
    type_of_visit_dropdown.select_by_visible_text("Day Visit")

    # %%
    today = datetime.today().strftime('%Y-%m-%d')
    today_element = driver.find_element(By.XPATH, ("//*[@id='app']/div/div/main/section/main/div/form/div[1]/div[2]/div/div/input"))
    today_element.send_keys(today)
    # %%
    #entering first name
    First_Name = os.getenv("FirstName")
    first_name_element = driver.find_element(By.XPATH, ("/html/body/div/div/div/main/section/main/div/form/div[1]/div[3]/div/div/input"))
    first_name_element.send_keys(First_Name)
    #entering surname
    Surname = os.getenv("Surname")
    surname_element = driver.find_element(By.XPATH, "//*[@id='surname']")
    surname_element.send_keys(Surname)
    #entering the mobile number
    phone_number = os.getenv("MobileNumber")
    phone_number_element = driver.find_element(By.XPATH, "//*[@id='app']/div/div/main/section/main/div/form/div[1]/div[5]/div/div/div/div/input")
    phone_number_element.send_keys(phone_number)
    #entering the email address
    email_address = os.getenv("EmailAddress")
    email_address_element = driver.find_element(By.XPATH, "//*[@id='email']")
    email_address_element.send_keys(email_address)
    #entering id number
    id_number = os.getenv("ID")
    id_number_element = driver.find_element(By.XPATH,"//*[@id='id_number']")
    id_number_element.send_keys(id_number)
    time.sleep(10)
    #book_visit = "#app > div > div > main > section > main > div > form > div.mt-8 > button"
    #book_visit_element = driver.find_element(By.CSS_SELECTOR, book_visit)
    #book_visit_element.click() 
    
