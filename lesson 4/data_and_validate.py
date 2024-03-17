import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://wikipedia.org/")

url = driver.current_url
print(f"URL  страницы: {url}")
assert url == "https://www.wikipedia.org/", "Test failed"


current_title = driver.title
print(f"Теукщий заголовок: {current_title}")

assert current_title == "Wikipedia", "Test failed"

print(driver.page_source)