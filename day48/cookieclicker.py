from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import re

timeout = time.time() + 5
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value="cookie")
while True:
    cookie.click()

    if time.time() > timeout:
        panel = driver.find_elements(By.CSS_SELECTOR, value="#rightPanel b")
        moneys = driver.find_element(By.ID, value="money")
        moneys = int(moneys.text)
        panels = []
        for pan in panel:
            panel_item = pan.text
            panels.append(panel_item.split(" - "))

        panels_price = [panels[i][1] for i in range(len(panels) - 1)]

        gray_panel = driver.find_elements(By.CLASS_NAME, value="grayed")
        gray_panels = []
        for g_pan in gray_panel:
            gray_panel_item = g_pan.text
            gray_panels.append(re.split("- |\n", gray_panel_item))

        gray_panels_price = [gray_panels[j][1] for j in range(len(gray_panel) - 1)]
        print(gray_panels_price)

        award = [award for award in panels_price if award not in gray_panels_price]
        select = award[len(award) - 1]
        result = [panels[i][0] for i in range(len(panels) - 1) if panels[i][1] == select]

        award_clicker = driver.find_element(By.XPATH, value=f'//*[@id="buy{result[0]}"]')
        award_clicker.click()

        timeout = time.time() + 5



# for i in panels:
#     if moneys >= panels[i] > panels[i - 1]:
#         must_click = panels[i]
#     else:
#         must_click = panels[i - 1]








