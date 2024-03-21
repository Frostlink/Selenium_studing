import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
action = ActionChains(driver)

# LEFT_CLICK_BUTTON_LOCATOR = ("xpath", "//button[@id='leftClick']")
# RIGHT_CLICK_BUTTON_LOCATOR = ("xpath", "//button[@id='rightClick']")
# DOUBLE_CLICK_LOCATOR = ("xpath", "//button[@id='doubleClick']")
# HOVER_BUTTON_LOCATOR = ("xpath", "//button[@id='colorChangeOnHover']")
MAIN_TWO = ("xpath", "//a[text()='Main Item 2']")
SUB = ("xpath", "//a[text()='SUB SUB LIST »']")
SUB2 = ("xpath", "//a[text()='Sub Sub Item 2']")

# driver.get("https://testkru.com/Elements/Buttons")
driver.get("https://demoqa.com/menu")

# left_button = driver.find_element(*LEFT_CLICK_BUTTON_LOCATOR)
# double_button = driver.find_element(*DOUBLE_CLICK_LOCATOR)
# right_click = driver.find_element(*RIGHT_CLICK_BUTTON_LOCATOR)
# hover_button = driver.find_element(*HOVER_BUTTON_LOCATOR)
main_2 = driver.find_element(*MAIN_TWO)
sub = driver.find_element(*SUB)
sub2 = driver.find_element(*SUB2)

time.sleep(3)

action.move_to_element(main_2)\
    .pause(2).move_to_element(sub).pause(2).move_to_element(sub2)\
    .pause(2).click(sub2).pause(2).perform()

# action.move_to_element(hover_button).perform()
# action.context_click(right_click).pause(2).double_click(double_button).pause(2).click(left_button).perform()
# action.context_click(right_click).perform()
# action.double_click(double_button).perform()
# action.click(left_button).perform()
time.sleep(3)