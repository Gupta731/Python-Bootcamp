from selenium import webdriver
from selenium.webdriver.chromium.service import ChromiumService
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

ACCOUNT_EMAIL = 'sourabh.gupta.731@gmail.com'
ACCOUNT_PASSWORD = 'Linked.11'
PHONE = 9609529801

edge_driver_path = 'C:/Edge Driver/msedgedriver.exe'
s = ChromiumService(edge_driver_path, start_error_message='Error')
driver = webdriver.ChromiumEdge(service=s)
driver.maximize_window()
driver.get('https://www.linkedin.com/jobs/search/?f_AL=true&geoId=102713980&keywords=python%20developer&location=India')
time.sleep(1.5)


def linkedin_login():
    driver.find_element(By.CLASS_NAME, 'nav__button-secondary').click()
    time.sleep(3)
    email = driver.find_element(By.ID, 'username')
    email.send_keys(ACCOUNT_EMAIL)
    password = driver.find_element(By.ID, 'password')
    password.send_keys(ACCOUNT_PASSWORD)
    driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button').click()
    time.sleep(10)


linkedin_login()

all_jobs = driver.find_elements(By.CSS_SELECTOR, '.job-card-container--clickable')
for job in all_jobs:
    job.click()
    time.sleep(1)
    try:
        driver.find_element(By.CSS_SELECTOR, '.jobs-apply-button').click()

        # If phone field is empty, then fill your phone number.
        phone = driver.find_element(By.CLASS_NAME, 'fb-single-line-text__input')
        if phone.text == '':
            phone.send_keys(PHONE)

        submit_button = driver.find_element(By.CSS_SELECTOR, 'footer button')

        # If the submit_button is a "Next" button, then this is a multi-step application, so skip.
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_elements(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()

        # Once application completed, close the pop-up window.
        time.sleep(2)
        close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        print('No application button, skipped.')
        continue

driver.quit()
