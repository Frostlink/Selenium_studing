import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import Keys

options = Options()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 5, poll_frequency=1)

MULTISELECT_LOCATOR = ("xpath", "//input[@id='react-select-4-input']")

driver.get("https://demoqa.com/select-menu")

driver.find_element(*MULTISELECT_LOCATOR).send_keys("Green" + Keys.TAB)

time.sleep(3)