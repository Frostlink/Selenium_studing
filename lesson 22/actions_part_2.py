import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
action = ActionChains(driver)



# 1 type
# driver.get("https://the-internet.herokuapp.com/drag_and_drop")
#
# COLLUMN_A = ("xpath", "//div[@id='column-a']")
# COLLUMN_B = ("xpath", "//div[@id='column-b']")
#
# A = driver.find_element(*COLLUMN_A)
# B = driver.find_element(*COLLUMN_B)
# time.sleep(2)
# action.drag_and_drop(A, B).perform()
# time.sleep(2)

# 2 type
driver.get("https://tympanus.net/Development/DragDropInteractions/sidebar.html")

GRID_ITEM = ("xpath", "//div[@class='grid__item'][3]")
SIDEBAR_ITEM = ("xpath", "//div[@class='drop-area__item'][3]")

grid = driver.find_element(*GRID_ITEM)
sidebar = driver.find_element(*SIDEBAR_ITEM)


action.click_and_hold(grid)\
    .pause(2)\
    .move_to_element(sidebar)\
    .release()\
    .perform()

time.sleep(5)
