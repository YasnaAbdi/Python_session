from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# import pyautogui
PROMISED_DOWN = 120
PROMISED_UP = 10
CHROME_DRIVER_PATH = "Users/Asus/.cache/selenium/chromedriver/win64/127.0.6533.99/chromedriver.exe"
reddit_url = "https://www.reddit.com/"
url = "https://www.speedtest.net/"


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.upload = 0
        self.download = 0

    def get_internet_speed(self):
        self.driver.get(url)

        go_btn = self.driver.find_element(By.XPATH,
                                          value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go_btn.click()

        sleep(60)

        self.download = self.driver.find_element(By.XPATH,
                                                 value='//*[@id=\"container\"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                       '3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        self.download = self.download.text

        self.upload = self.driver.find_element(By.XPATH,
                                               value='//*[@id=\"container\"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                     '3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.upload = self.upload.text

    def tweet_at_provider(self):
        self.driver.switch_to.window(reddit_url)
        sleep(10)
        comment_btn = self.driver.find_element(By.XPATH, value='//*[@id="t3_1ept7ej"]//div[2]/a')
        comment_btn.click()
        sleep(10)
        comment = self.driver.find_element(By.XPATH,
                                           value='//*[@id="main-content"]/shreddit-async-loader/comment-body-header/shreddit-async-loader[1]/comment-composer-host/faceplate-tracker[1]/button')
        comment.click()
        comment.send_keys("yes")
        sleep(10)
        send_comment = self.driver.find_element(By.XPATH,
                                                value='//*[@id="main-content"]/shreddit-async-loader/comment-body-header/shreddit-async-loader[1]/comment-composer-host/faceplate-form/shreddit-composer/button[2]/span/span/span')
        send_comment.click()
        self.driver.quit()


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()

# pyautogui.locateOnScreen(image="unnamed.png", confidence=0.5)
# pyautogui.click()
