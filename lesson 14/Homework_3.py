import time
import os
import pickle
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options )
wait = WebDriverWait(driver, 5, poll_frequency=1)

driver.get("https://www.amazon.ae/gp/cart/view.html?ref_=nav_top_cart")
time.sleep(10)
pickle.dump(driver.get_cookies(), open(os.getcwd()+'\mazon_cookies.pkl', 'wb'))

driver.delete_all_cookies()
driver.refresh()
time.sleep(10)
cookies = pickle.load(open(os.getcwd()+'\mazon_cookies.pkl', 'rb'))

for cookie in cookies:
    driver.add_cookie(cookie)

driver.refresh()

time.sleep(10)

