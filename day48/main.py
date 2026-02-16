from selenium import webdriver
from selenium.webdriver.common.by import By

# keep chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")
price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_cent = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
print(f"The price is {price_dollar.text}.{price_cent.text}")

driver.close()
events = {}
event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_year = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time span")
event_name = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

for n in range(len(event_times)):
    events[n] = {
        "time": event_year[n].text + event_times[n].text,
        "name": event_name[n].text,
    }

print(events)


driver.quit()