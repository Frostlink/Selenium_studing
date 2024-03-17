import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.freeconferencecall.com/login?campaing_tag=FCC20_WEB_ABA_0006")
time.sleep(5)
driver.find_element("id", "loginformsubmit").click()
time.sleep(5)
