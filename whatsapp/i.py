
# selenium
# gspread (برای ارتباط با Google Sheets)
# oauth2client (برای احراز هویت گوگل)
# احراز هویت به حساب گوگل و دسترسی به فایل گوگل شیتس.
#
# استفاده از Selenium برای اتوماسیون واتساپ وب.
#
# ارسال پیام به شمارهها.
#
# نصب پیشنیازها:
# برای نصب کتابخانههای مورد نیاز از این دستورات استفاده کنید:
#
# bash
# Copy code
# pip install selenium
# pip install gspread oauth2client
# کد:
# python
# Copy code
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import time

chrome_options = Options()
chrome_options.add_argument("--user-data-dir=./User_Data")


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://web.whatsapp.com')
print("لطفاً در واتساپ وب لاگین کنید.")
time.sleep(30)

driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get('https://docs.google.com/spreadsheets')
print("لطفاً در گوگل داک وب لاگین کنید.")
time.sleep(30)

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

spreadsheet = client.open('https://docs.google.com/spreadsheets/d/1JdLRFRoSRLjwn0OOe7iAoe29y72Zn8_BeGPMjoZLJy4/edit?gid=0#gid=0').sheet1
numbers = spreadsheet.col_values(1)

driver.switch_to.window(driver.window_handles[0])

for number in numbers:
    whatsapp_url = f"https://web.whatsapp.com/send?phone={number}"
    driver.get(whatsapp_url)
    time.sleep(10)

    message_box = driver.find_element(By.XPATH, '//div[@title="Type a message"]')
    message_box.send_keys("zendeghi an ast")
    message_box.send_keys(Keys.ENTER)
    time.sleep(5)

driver.quit()

# توضیحات کد:
# ورود به واتساپ وب: کروم با استفاده از Selenium باز شده و شما باید به صورت دستی QR Code را اسکن کنید تا وارد واتساپ وب شوید.
# دسترسی به گوگل شیتس: این مرحله با استفاده از کتابخانه gspread و یک فایل JSON برای احراز هویت گوگل انجام میشود. شما باید از Google Cloud Console کلید API خود را دانلود کنید.
# دریافت شمارهها از شیتس: شمارهها از ستون اول گوگل شیتس خوانده شده و در متغیر numbers ذخیره میشوند.
# ارسال پیام: برای هر شماره، یک چت جدید باز میشود و پیام ارسال میگردد.
# مراحل بعدی:
# برای استفاده از Google Sheets API باید یک پروژه در Google Cloud Console ایجاد کرده و دسترسی به Google Sheets API را فعال کنید.
# فایل JSON احراز هویت (credentials.json) را دانلود کرده و در همان پوشه کد قرار دهید.
# در صورت نیاز به راهنمایی بیشتر در هر بخش، من میتوانم شما را همراهی کنم.