import time
import os
import pickle
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options )
wait = WebDriverWait(driver, 5, poll_frequency=1)

driver.get("https://dzen.ru/")

driver.add_cookie({
    "name": "username",
    "value": "user123"
})

driver.refresh()

driver.get_cookie("username"), "BAD"