import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(3)
print(driver.find_element("class name", "wikipedia-icon"))
time.sleep(3)
print(driver.find_element("class name", "wikipedia-search-wiki-link"))
time.sleep(3)