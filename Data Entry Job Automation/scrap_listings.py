from bs4 import BeautifulSoup
import requests
import re
from nltk import flatten

ZILLOW_URL = 'https://bit.ly/2VDzfb2'
ZILLOW_HEADERS = {
    'User-Agent': 'Defined',
    'Accept-Language': 'en-GB,en;q=0.9,en-US;q=0.8',
}


class GetListings:
    def __init__(self):
        self.response = requests.get(url=ZILLOW_URL, headers=ZILLOW_HEADERS)
        self.response.raise_for_status()
        self.soup = BeautifulSoup(self.response.text, 'lxml')
        self.property_listings = []

    def get_listing_details(self):
	"""Scraps the zillow real estate posting website to get details like address, price and link to the post"""
        listing_address = [item.text for item in self.soup.select(selector='.photo-cards_short li address')]
        listing_price = flatten([re.findall(r"\$[\w]+,[\w]+", item.text) for item in
                                 self.soup.select(selector='.photo-cards_short li .list-card-price')])
        listing_link = [item['href'] for item in self.soup.select(selector='.list-card-info a')]
        for n, link in enumerate(listing_link):
            if re.search(r"https://[-?_=./\w]+", link) is None:
                listing_link[n] = 'https://www.zillow.com' + link

        for item in zip(listing_address, listing_price, listing_link):
            self.property_listings.append(item)
        return self.property_listings
