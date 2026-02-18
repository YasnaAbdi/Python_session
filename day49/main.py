import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

url = ("https://www.linkedin.com/jobs/search/?currentJobId=3989047029&f_LF=f_AL&geoId=102257491&keywords=python"
       "%20developer&location=London%2C%20England%2C%20United%20Kingdom")
emil = "yasnaabdi2024@gmail.com"
passcode = "jungkook,11997"
PHONE = "01234567890"


def abort_application():
    # Click Close Button
    close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_button.click()

    time.sleep(2)
    # Click Discard Button
    discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
    discard_button.click()


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

time.sleep(2)
sign_in_button = driver.find_element(by=By.LINK_TEXT, value="Sign in")
sign_in_button.click()

username = driver.find_element(By.ID, value="username")
username.send_keys(emil)

password = driver.find_element(By.ID, value="password")
password.send_keys(passcode)

sign_btn = driver.find_element(By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button')
sign_btn.send_keys(Keys.ENTER)

# Get Listings
time.sleep(5)
all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")

# Apply for Jobs
for listing in all_listings:
    print("Opening Listing")
    listing.click()
    time.sleep(2)
    try:
        # Click Apply Button
        apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
        apply_button.click()

        # Insert Phone Number
        # Find an <input> element where the id contains phoneNumber
        time.sleep(5)
        phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
        if phone.text == "":
            phone.send_keys(PHONE)

        # Check the Submit Button
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            abort_application()
            print("Complex application, skipped.")
            continue
        else:
            # Click Submit Button
            print("Submitting job application")
            submit_button.click()

        time.sleep(2)
        # Click Close Button
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        abort_application()
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()
