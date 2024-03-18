import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

options = Options()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument("--windows-size=1920,1080")
options.add_argument("--disable-blink-features=AutomationControlled")
service = Service(executable_path=ChromeDriverManager().install())
user1 = webdriver.Chrome(options=options)
wait = WebDriverWait(user1, 5, poll_frequency=1)

LOGIN_FIELD = ("xpath", "//input[@type='email']")
PASSWORD_FIELD = ("xpath", "//input[@type='password']")
SUBMIT_BUTTON = ("xpath", "//button[@type='submit']")

user1.get("https://hyperskill.org/login")
user1.find_element(*LOGIN_FIELD).send_keys("te222st@mail.ru")
user1.find_element(*PASSWORD_FIELD).send_keys("123433567password")
user1.find_element(*SUBMIT_BUTTON).click()
time.sleep(5)

user2 = webdriver.Chrome(options=options)
user2.get("https://hyperskill.org/login")
user2.find_element(*LOGIN_FIELD).send_keys("te212322st@mail.ru")
user2.find_element(*PASSWORD_FIELD).send_keys("123433567password")
user2.find_element(*SUBMIT_BUTTON).click()
time.sleep(5)