from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 30, poll_frequency=1)
driver.get("https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver")

CHANGE_TEXT = ("xpath", "//button[@id='populate-text']")
TEXT_H2 = ("id", "h2")
DISPLAY_BUTTON = ("xpath", "//button[@id='display-other-button']")
HIDDEN_BUTTON = ("xpath", "//button[@id='hidden']")
DISABLED_BUTTON = ("xpath", "//button[@id='disable']")
ENABLE_BUTTON = ("xpath", "//button[@id='enable-button']")
CLICK_ME_TO_OPEN = ("xpath", "//button[@id='alert']")

# case 1
driver.find_element(*CHANGE_TEXT).click()
assert wait.until(EC.text_to_be_present_in_element(TEXT_H2, "Selenium Webdriver")), "Case 1 Failed"


# case 2
driver.find_element(*DISPLAY_BUTTON).click()
assert wait.until(EC.visibility_of_element_located(HIDDEN_BUTTON)), "Case 2 Failed"

# case 3
driver.find_element(*ENABLE_BUTTON).click()
assert wait.until(EC.element_to_be_clickable(DISABLED_BUTTON)), "Case 3 Failed"

# case 4
driver.find_element(*CLICK_ME_TO_OPEN).click()
assert wait.until(EC.alert_is_present()), "Case 4 Failed"
