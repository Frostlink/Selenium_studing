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

KEYBOARD_INPUT = ("xpath", "//input[@id='target']")

driver.get("https://the-internet.herokuapp.com/key_presses")
time.sleep(3)
driver.find_element(*KEYBOARD_INPUT).send_keys("A123123123")
time.sleep(3)
driver.find_element(*KEYBOARD_INPUT).send_keys(Keys.CONTROL + "A")
time.sleep(3)
driver.find_element(*KEYBOARD_INPUT).send_keys(Keys.BACKSPACE)
time.sleep(3)