from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://hyperskill.org/tracks")
#Header

LOGO = driver.find_elements("xpath", "//a[@class='nav-link']")


#Body

ALL_TRACKS_TAB = driver.find_elements("xpath", "//button[contains(@class, 'btn text-nowrap')]")

print(LOGO)
print(ALL_TRACKS_TAB)