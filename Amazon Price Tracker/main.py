import os
import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

AMAZON_PRODUCT_URL = 'https://www.amazon.in/Dell-inch-60-96cm-Full-Monitor/dp/B07FDNTS33'
EXPECTED_PRICE = 16000.00
AMAZON_HEADERS = {
    'User-Agent': 'Defined',
    'Accept-Language': 'en-GB,en;q=0.9,en-US;q=0.8',
}
MY_EMAIL = 'sourabhmahan@gmail.com'
TO_EMAIL = 'tiu.f2.cse@gmail.com'
PASSWORD = os.environ.get('PASSWORD')

response = requests.get(url=AMAZON_PRODUCT_URL, headers=AMAZON_HEADERS)
response.raise_for_status()
soup = BeautifulSoup(response.text, 'html.parser')
name_of_product = soup.find(name='span', id='productTitle').text.strip()
price = float(soup.find(name='span', id='priceblock_ourprice').text.strip('₹').replace(',', ''))

if price <= EXPECTED_PRICE:
    msg = MIMEMultipart()
    msg['To'] = TO_EMAIL
    msg['From'] = f"Saurabh Gupta <{MY_EMAIL}>"
    msg['Subject'] = 'Amazon Price Alert!'
    msg['Content-Type'] = "text/html; charset=utf-8"
    msg_text = MIMEText(f"{name_of_product} is now ₹{price}\n{AMAZON_PRODUCT_URL}\n\n"
                        f"<sent from my python automated Amazon Price Tracker>")
    msg.attach(msg_text)
    try:
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=TO_EMAIL, msg=msg.as_string())
            print('Notification Sent.')
    except Exception as e:
        print('Unable to send email.')
