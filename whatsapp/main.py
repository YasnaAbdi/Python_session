import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import ui

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://workspace.google.com/products/sheets/")

time.sleep(3)

google = driver.find_element(By.TAG_NAME, 'gws-button')
google.click()

email_input = driver.find_element(By.TAG_NAME, 'input')
email_input.send_keys('yasnaabdi2003@gmail.com')

login_btn = driver.find_element(By.CLASS_NAME, 'VfPpkd-RLmnJb')
login_btn.click()

# openWindow(url, windowId)
# waitForPopup(windowId, timeout)
# selectwindow(windowId)
#
# current_window = driver.current_window_handle
# parent = driver.window_handles[0]
# child = driver.window_handles[1]
# driver.switch_to.window(child)
#
# driver.switch_to.window(parent)



