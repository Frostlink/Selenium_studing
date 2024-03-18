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

# SELECT_LOCATOR = ("xpath", "//input[@id='react-select-3-input']")
SELECT_ONE = ("xpath", "//div[@id='selectOne']")
PROF_OPTION = ("xpath", "//div[text()='Prof.']")

driver.get("https://demoqa.com/select-menu")


# time.sleep(3)
# driver.find_element(*SELECT_LOCATOR).send_keys("Ms." + Keys.ENTER)
# time.sleep(3)

time.sleep(3)
driver.find_element(*SELECT_ONE).click()
time.sleep(3)
driver.find_element(*PROF_OPTION).click()
time.sleep(3)