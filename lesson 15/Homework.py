import time

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

driver.get("https://demoqa.com/selectable")

GRID = ("xpath", "//a[@id='demo-tab-grid']")
ONE = ("xpath", "//li[text()='One']")
FIVE = ("xpath", "//li[text()='Five']")
NINE = ("xpath", "//li[text()='Nine']")

driver.find_element(*GRID).click()
time.sleep(3)
driver.find_element(*ONE).click()
one_check = driver.find_element(*ONE).get_attribute("class")
assert "active" in one_check
time.sleep(3)
driver.find_element(*FIVE).click()
five_check = driver.find_element(*FIVE).get_attribute("class")
assert "active" in five_check
time.sleep(3)
driver.find_element(*NINE).click()
nine_check = driver.find_element(*NINE).get_attribute("class")
assert "active" in nine_check
time.sleep(3)