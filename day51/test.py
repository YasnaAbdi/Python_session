from selenium import webdriver

driver = webdriver.Chrome()

print(driver.service.path)