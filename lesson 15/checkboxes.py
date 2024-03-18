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
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 5, poll_frequency=1)

driver.get("https://demoqa.com/radio-button")

YES_RADIO_STATUS = ("xpath", "//input[@id='yesRadio']")
YES_RADIO = ("xpath", "//label[@for='yesRadio']")
NO_RADIO_STATUS = ("xpath", "//input[@id='noRadio']")
NO_RADIO = ("xpath", "//label[@for='noRadio']")

# print(driver.find_element(*YES_RADIO_STATUS).is_selected())
# driver.find_element(*YES_RADIO).click()
# print(driver.find_element(*YES_RADIO_STATUS).is_selected())

print(driver.find_element(*NO_RADIO_STATUS).is_enabled())