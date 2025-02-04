from selenium import webdriver
import undetected_chromedriver as uc

def create_driver(user_agent):
    options = webdriver.ChromeOptions()
    options.add_argument(f'--user-agent={user_agent}')
    options.add_argument("--window-size=1920,1080")
    options.headless = False

    options.add_argument("--lang=en-GB") # change language

    driver = uc.Chrome(options=options)

    return driver