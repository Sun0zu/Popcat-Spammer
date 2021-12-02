
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent
from selenium import webdriver
from time import sleep

def open_browser():
    global driver
    options = webdriver.ChromeOptions()
    options.add_argument("--log-level=3")
    ua = UserAgent()
    user_agent = ua.random
    options.add_argument(f'user-agent={user_agent}')
    driver = webdriver.Chrome(options=options, executable_path=r#'Remove the hashtag and enter the path',)
    driver.get('https://popcat.click/')
    sleep(4)
    spam_click()

def spam_click():
    while True:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
         '/html/body/div[1]/div'))).click()

open_browser()