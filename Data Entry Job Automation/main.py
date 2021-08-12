from selenium import webdriver
from selenium.webdriver.chromium.service import ChromiumService
from selenium.webdriver.common.by import By
from scrap_listings import GetListings
from time import sleep

FORMS_URL = 'https://forms.gle/7irrwBxHUxDSBB63A'
EDGE_DRIVER_PATH = 'C:/Edge Driver/msedgedriver.exe'


class DataEntry:
    def __init__(self):
        self.s = ChromiumService(EDGE_DRIVER_PATH, start_error_message='error')
        self.driver = webdriver.ChromiumEdge(service=self.s)
        self.driver.maximize_window()

    def submit_data(self):
		"""Uses Selenium web driver to repeatedly fill the google form and submit the data for all the postings in zillow website"""
        for data in property_data:
            self.driver.get(FORMS_URL)
            sleep(3)
            address_input = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/'
                                                               'div[2]/div/div[1]/div/div[1]/input')
            address_input.send_keys(data[0])
            price_input = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/'
                                                             'div[2]/div/div[1]/div/div[1]/input')
            price_input.send_keys(data[1])
            link_input = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/'
                                                            'div[2]/div/div[1]/div/div[1]/input')
            link_input.send_keys(data[2])
            sleep(1)
            submit_button = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/'
                                                               'span')
            submit_button.click()
            sleep(1)
        self.driver.close()


listing = GetListings()
property_data = listing.get_listing_details()
data_entry = DataEntry()
data_entry.submit_data()
