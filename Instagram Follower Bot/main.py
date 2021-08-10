from selenium import webdriver
from selenium.webdriver.chromium.service import ChromiumService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, \
    StaleElementReferenceException
from time import sleep

EMAIL = YOUR_EMAIL_HERE
PASSWORD = INSTAGRAM_PASSWORD
TARGET_ACCOUNT = SOME_INSTA_ACCOUNT
EDGE_DRIVER_PATH = 'C:/Edge Driver/msedgedriver.exe'


class InstaFollower:
    def __init__(self):
        self.s = ChromiumService(EDGE_DRIVER_PATH, start_error_message='error')
        self.driver = webdriver.ChromiumEdge(service=self.s)
        self.driver.maximize_window()

    def login(self):
		"""Login to Instagram and dismiss all popups"""
        self.driver.get('https://www.instagram.com/accounts/login/')
        sleep(5)
        user_name = self.driver.find_element(By.NAME, 'username')
        user_name.send_keys(EMAIL)
        password = self.driver.find_element(By.NAME, 'password')
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)
        sleep(8)
        try:
            no_notifications = self.driver.find_element(By.CSS_SELECTOR, '.HoLwm')
            no_notifications.click()
        except NoSuchElementException:
            not_now_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/'
                                                                'button')
            not_now_button.click()
            sleep(8)
            no_notifications = self.driver.find_element(By.CSS_SELECTOR, '.HoLwm')
            no_notifications.click()

        sleep(5)

    def find_followers(self):
		"""Find followers of a target account"""
        self.driver.get(f'https://www.instagram.com/{TARGET_ACCOUNT}')
        sleep(10)
        followers = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/'
                                                       'ul/li[2]/a')
        followers.click()
        sleep(5)

    def follow(self):
		"""Follow all the followers of the target account"""
        popup = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div[2]')
        for i in range(2):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;",
                                       popup)
            sleep(1)
        follow_buttons = self.driver.find_elements(By.CSS_SELECTOR, '.wo9IH button')
        for button in follow_buttons:
            try:
                button.click()
                sleep(1)
            except ElementClickInterceptedException:
                sleep(1)
                cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div[3]/button[2]')
                cancel_button.click()
                sleep(1)
            except NoSuchElementException:
                sleep(3)

        try:
            close_popup = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div[1]/div/div[2]/button')
            close_popup.click()
            sleep(1)
        except ElementClickInterceptedException:
            cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div[3]/button[2]')
            cancel_button.click()
            sleep(1)
            close_popup = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div[1]/div/div[2]/button')
            close_popup.click()
            sleep(1)

    def logout(self):
		"""Logout of Instagram"""
        profile_button = self.driver.find_element(By.CSS_SELECTOR, '.qNELH')
        profile_button.click()
        sleep(1)
        buttons_near_logout = self.driver.find_elements(By.CSS_SELECTOR, '.xLCgt')
        for button in buttons_near_logout:
            try:
                if button.text == 'Log Out':
                    button.click()
            except StaleElementReferenceException:
                pass
        sleep(2)
        self.driver.close()


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
bot.logout()
