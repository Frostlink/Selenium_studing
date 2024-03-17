import os
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
prefs = {
   "download.default_directory": f"{os.getcwd()}\down"
}
chrome_options.add_experimental_option("prefs", prefs)
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://demoqa.com/upload-download")
down = driver.find_element("xpath", "//a[@id='downloadButton']")
up = driver.find_element("xpath", "//input[@type='file']" )
time.sleep(3)

down.click()

time.sleep(3)

up.send_keys(f"{os.getcwd()}\down\sampleFile.jpeg")

time.sleep(3)