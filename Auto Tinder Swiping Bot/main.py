from selenium import webdriver
from selenium.webdriver.chromium.service import ChromiumService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from time import sleep

FB_EMAIl = YOUR_EMAIL_HERE
FB_PASSWORD = YOUR_PASSWORD_HERE

edge_driver_path = 'C:/Edge Driver/msedgedriver.exe'
s = ChromiumService(edge_driver_path, start_error_message='error')
driver = webdriver.ChromiumEdge(service=s)
driver.maximize_window()
driver.get('https://tinder.com/')


def login_to_tinder():
    sleep(15)
    login_button = driver.find_element(By.XPATH, '//*[@id="o-738591094"]/div/div[1]/div/main/div[1]/div/div/div/div/'
                                                 'header/div/div[2]/div[2]/a')

    login_button.click()

    sleep(7)
    more_options = driver.find_element(By.XPATH, '//*[@id="o1827995126"]/div/div/div[1]/div/div[3]/span/button')
    if more_options.text == 'MORE OPTIONS':
        more_options.click()

    sleep(5)
    fb_login = driver.find_element(By.XPATH, '//*[@id="o1827995126"]/div/div/div[1]/div/div[3]/span/div[2]/button')
    fb_login.click()

    sleep(10)


def login_with_fb():
    sleep(5)
    base_window = driver.window_handles[0]
    fb_window = driver.window_handles[1]
    driver.switch_to.window(fb_window)

    fb_email = driver.find_element(By.XPATH, '//*[@id="email"]')
    fb_email.send_keys(FB_EMAIl)
    fb_password = driver.find_element(By.XPATH, '//*[@id="pass"]')
    fb_password.send_keys(FB_PASSWORD)
    fb_password.send_keys(Keys.ENTER)

    sleep(10)
    driver.switch_to.window(base_window)


def handle_popups():
    sleep(3)
    location = driver.find_element(By.XPATH, '//*[@id="o1827995126"]/div/div/div/div/div[3]/button[1]')
    location.click()
    sleep(3)
    notification = driver.find_element(By.XPATH, '//*[@id="o1827995126"]/div/div/div/div/div[3]/button[2]')
    notification.click()
    # Allow cookies
    # sleep(3)
    # cookies = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/div/div/div[1]/button')
    # cookies.click()
    sleep(10)


def like_profiles():
    sleep(15)
    for i in range(10):
        try:
            if i == 1:
                like_button = driver.find_element(By.XPATH, '//*[@id="o-738591094"]/div/div[1]/div/main/div[1]/div/div/'
                                                            'div[1]/div[1]/div/div[4]/div/div[4]/button')
            else:
                like_button = driver.find_element(By.XPATH, '//*[@id="o-738591094"]/div/div[1]/div/main/div[1]/div/div/'
                                                            'div[1]/div[1]/div/div[5]/div/div[4]/button')
            like_button.click()
            sleep(5)

        except NoSuchElementException:
            print('cannot like')
            sleep(3)
        except ElementClickInterceptedException:
            no_add_to_home = driver.find_element(By.XPATH, '//*[@id="o1827995126"]/div/div/div[2]/button[2]')
            no_add_to_home.click()
            sleep(3)


login_to_tinder()
login_with_fb()
handle_popups()
like_profiles()
