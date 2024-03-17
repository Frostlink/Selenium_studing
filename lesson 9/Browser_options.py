import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.page_load_strategy = "eager"
#chrome_options.add_argument("--headless")
#chrome_options.add_argument("--incognito")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--disable-cache")
#chrome_options.add_argument("--window-size=2560,1440")
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
#driver.maximize_window()

start_time = time.time()
driver.get("https://whatismyipaddress.com/")
end_time = time.time()
result = end_time - start_time
print(result)

#driver.get("https://expired.badssl.com/")

