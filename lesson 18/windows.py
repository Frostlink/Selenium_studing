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
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 5, poll_frequency=1)

driver.switch_to.new_window("window")
time.sleep(3)

driver.get("https://ya.ru")

# FOR_BUSINESS_BUTTON_LOCATOR = ("xpath", "//a[text()=' For Business ']")
# START_FREE_BUTTON_LOCATOR = ("xpath", "//a[text()='Start for Free']")

# driver.get("https://hyperskill.org/tracks")
# time.sleep(3)
#
# windows = driver.window_handles
#
# driver.switch_to.window(windows[1])
# driver.get("https://ya.ru")

# print(driver.current_window_handle)
# print(driver.window_handles)
#
# driver.find_element(*FOR_BUSINESS_BUTTON_LOCATOR).click()
# time.sleep(3)
#
# tabs = driver.window_handles
# driver.switch_to.window(tabs[1])
#
# driver.find_element(*START_FREE_BUTTON_LOCATOR).click()
# time.sleep(3)