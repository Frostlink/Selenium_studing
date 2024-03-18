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
options.add_argument("--windows-size=1920:1080")
options.add_argument("--disable-blink-features=AutomationControlled")
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 5, poll_frequency=1)

#task 1
driver.get("https://hyperskill.org/login")
driver.switch_to.new_window("tab")
driver.get("https://www.ya.ru/")
driver.switch_to.new_window("tab")
driver.get("https://www.dzen.ru/")

tabs = driver.window_handles

#task 2
HYPER_TITLE = ("xpath", "//title")
YA_TITLE = ("xpath", "//title")
DZEN_TITLE = ("xpath", "//title")

driver.switch_to.window(tabs[0])
print(driver.find_element(*HYPER_TITLE).get_attribute("text"))
time.sleep(3)

driver.switch_to.window(tabs[1])
print(driver.find_element(*YA_TITLE).get_attribute("text"))
time.sleep(3)

driver.switch_to.window(tabs[2])
print(driver.find_element(*DZEN_TITLE).get_attribute("text"))
time.sleep(3)

#task 3
HYPER_BUTTON = ("xpath", "//a[text()=' Pricing ']")
YANDEX_BUTTON = ("xpath", "//a[@data-statlog='2informers.weather']")
DZEN_BUTTON = ("xpath", "//div[text()='Симферополь']")

driver.switch_to.window(tabs[0])
driver.find_element(*HYPER_BUTTON).click()
time.sleep(3)

driver.switch_to.window(tabs[1])
driver.find_element(*YANDEX_BUTTON).click()
time.sleep(3)

driver.switch_to.window(tabs[2])
driver.find_element(*DZEN_BUTTON).click()
time.sleep(3)


