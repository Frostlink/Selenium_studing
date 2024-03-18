import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument("--windows-size=1920,1080")
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(options=options)

# FORM_NAME_FIELD_LOCATOR = ("xpath", "//input[@id='RESULT_TextField-0']")
# BUUTON_COPY_LOCATOR = ("xpath", "button[text()='Copy Text']")
#
# driver.get("https://testautomationpractice.blogpost.com/")
# driver.switch_to.frame(0)
# time.sleep(3)
# driver.find_element(*FORM_NAME_FIELD_LOCATOR).send_keys("Privetik")
# time.sleep(3)
#
# driver.switch_to.default_content()
#
# driver.find_element(*BUUTON_COPY_LOCATOR).click()
# time.sleep(3)

driver.get("https://demoqa.com/nestedframes")
driver.switch_to.frame("frame1")
print(driver.find_element("xpath", "//body").text)

driver.switch_to.frame(0)
print(driver.find_element("xpath", "//body").text)

driver.switch_to.parent_frame()
print(driver.find_element("xpath", "//body").text)

driver.switch_to.default_content()
