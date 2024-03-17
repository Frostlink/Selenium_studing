import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://demoqa.com/text-box")

name = driver.find_element("xpath", "//input[@id='userName']")
email = driver.find_element("xpath", "//input[@id='userEmail']")
Current_Address = driver.find_element("xpath", "//textarea[@id='currentAddress']")
Permanent_Address = driver.find_element("xpath", "//textarea[@id='permanentAddress']")


assert name.get_attribute("value") == "", "Name isn't empty"
assert email.get_attribute("value") == "", "Email isn't empty"
assert Current_Address.get_attribute("value") == "", "Current Address isn't empty"
assert Permanent_Address.get_attribute("value") == "", "Permanent Address isn't empty"


name.send_keys("Kirill Tuta")
email.send_keys("kirill@mail.com")
Current_Address.send_keys("Moscow, Kreml")
Permanent_Address.send_keys("Dubai, Marina")

assert name.get_attribute("value") == "Kirill Tuta", "Name isn't it after input"
assert email.get_attribute("value") == "kirill@mail.com", "Email isn't it after input"
assert Current_Address.get_attribute("value") == "Moscow, Kreml", "Current Address isn't it after input"
assert Permanent_Address.get_attribute("value") == "Dubai, Marina", "Permanent Address isn't it after input"
