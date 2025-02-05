from selenium import webdriver
import undetected_chromedriver as uc

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