from selenium import webdriver
from selenium.webdriver.chromium.service import ChromiumService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from time import sleep
import os

EMAIl = 'sourabhmahan@gmail.com'
PASSWORD = os.environ.get('PASSWORD')
PROMISED_UP = 5
PROMISED_DOWN = 5
EDGE_DRIVER_PATH = 'C:/Edge Driver/msedgedriver.exe'


class InternetSpeedTwitterBot:
    def __init__(self):
        self.s = ChromiumService(EDGE_DRIVER_PATH, start_error_message='error')
        self.driver = webdriver.ChromiumEdge(service=self.s)
        self.driver.maximize_window()
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        """Gets the internet speed for speed test website"""
        self.driver.get('https://www.speedtest.net/')
        sleep(10)
        try:
            check_speed = self.driver.find_element(By.CLASS_NAME, 'start-text')
            check_speed.click()
            sleep(45)
            self.down = float(self.driver.find_element(By.CSS_SELECTOR, '.download-speed').text)
            self.up = float(self.driver.find_element(By.CSS_SELECTOR, '.upload-speed').text)
        except (NoSuchElementException, ElementClickInterceptedException):
            print('Some elements not found while checking speed')
        else:
            print(f'Down: {self.down}')
            print(f'Up: {self.up}')
        sleep(4)

    def tweet_at_provider(self):
        """Logs in and tweets to ISP complaining about the internet speed and then logs out"""
        self.driver.get('https://twitter.com/login')
        sleep(4)
        email_input = self.driver.find_element(By.NAME, 'session[username_or_email]')
        email_input.send_keys(EMAIl)
        pass_input = self.driver.find_element(By.NAME, 'session[password]')
        pass_input.send_keys(PASSWORD)
        pass_input.send_keys(Keys.ENTER)
        sleep(8)

        try:
            tweet_area = self.driver.find_element(By.CSS_SELECTOR, '.public-DraftStyleDefault-ltr')
            tweet_area.send_keys(f'Hey <Internet Provider>, why is my internet speed (Down: {self.down}/Up: {self.up}) '
                                 f'when I pay for 4G?\nTweeted by my Bot made using Python and Selenium WebDriver.')
            tweet_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/'
                                                              'div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/'
                                                              'div[3]/div/div/div[2]/div[3]')
            tweet_button.click()
            sleep(8)

            account_options = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/'
                                                                 'div/div[2]/div/div')
            account_options.click()
            sleep(2)
            logout = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div[2]/div/div[2]/div/div/'
                                                        'div/div/div/a[2]')
            logout.click()
            sleep(2)
            self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div[3]/'
                                               'div[2]/div').click()
            sleep(5)
            self.driver.close()
        except (NoSuchElementException, ElementClickInterceptedException):
            print('Some elements not found in twitter page.')


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
if bot.down < PROMISED_DOWN or bot.up < PROMISED_UP:
    bot.tweet_at_provider()
