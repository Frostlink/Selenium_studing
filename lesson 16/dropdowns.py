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
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 5, poll_frequency=1)

SELECT_LOCATOR = ("xpath", "//select[@id='dropdown']")

driver.get("https://the-internet.herokuapp.com/dropdown")

DROPDOWN = Select(driver.find_element(*SELECT_LOCATOR))
all_optins = DROPDOWN.options

# DROPDOWN.select_by_visible_text("Option 1")
# DROPDOWN.select_by_value("2")
# DROPDOWN.select_by_index(1)

# Перебор по тексту
# for option in all_optins:
#     time.sleep(1)
#     if "Option 1" in option.text: print("OK")
#     DROPDOWN.select_by_visible_text(option.text)

# Перебор по индексу

# for option in all_optins:
#     time.sleep(1)
#     DROPDOWN.select_by_index(all_optins.index(option))

# Перебор по value
for option in all_optins:
    time.sleep(1)
    DROPDOWN.select_by_value(option.get_attribute("value"))