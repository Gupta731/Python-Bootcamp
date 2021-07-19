import datetime as dt
import os

import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

STOCK = "TSLA"
COMPANY_NAME = "Tesla"
STOCK_PRICE_API = 'https://www.alphavantage.co/query'
STOCK_PRICE_API_KEY = os.environ.get('STOCK_PRICE_API_KEY')
STOCK_NEWS_API = 'https://newsapi.org/v2/everything'
STOCK_NEWS_API_KEY = os.environ.get('STOCK_NEWS_API_KEY')
MY_EMAIL = 'sourabhmahan@gmail.com'
TO_EMAIL = 'tiu.f2.cse@gmail.com'
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

yesterday_date = str(dt.date.today() - dt.timedelta(days=1))
before_yesterday = str(dt.date.today() - dt.timedelta(days=2))
news_titles = []
news_brief = []


def get_stock_percentage_change():
    price_parameters = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': STOCK,
        'apikey': STOCK_PRICE_API_KEY,
    }

    price_response = requests.get(url=STOCK_PRICE_API, params=price_parameters)
    price_response.raise_for_status()
    price_data = price_response.json()['Time Series (Daily)']
    yesterday_price_data = float(price_data[yesterday_date]['4. close'])
    before_yesterday_price_data = float(price_data[before_yesterday]['4. close'])
    percentage_change = round(((yesterday_price_data - before_yesterday_price_data) /
                               before_yesterday_price_data) * 100, 2)
    return percentage_change


def get_stock_news():
    news_parameters = {
        'q': COMPANY_NAME,
        'from': before_yesterday,
        'language': 'en',
        'sortBy': 'date',
        'apiKey': STOCK_NEWS_API_KEY,
    }
    news_response = requests.get(url=STOCK_NEWS_API, params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()['articles'][:3]

    for data in news_data:
        news_titles.append(data['title'])
        news_brief.append(data['description'])


def send_email(percentage_change, arrow):
    get_stock_news()
    msg = MIMEMultipart()
    msg['To'] = TO_EMAIL
    msg['From'] = MY_EMAIL
    msg['Subject'] = f"{COMPANY_NAME}: {arrow}{percentage_change}"
    msg['Content-Type'] = "text/html; charset=utf-8"
    msg_text = MIMEText(f"Here are the top 3 headlines:\n\n"
                        f"Headline: {news_titles[0]}.\nBrief: {news_brief[0]}.\n\n"
                        f"Headline: {news_titles[1]}.\nBrief: {news_brief[1]}.\n\n"
                        f"Headline: {news_titles[2]}.\nBrief: {news_brief[2]}.")
    msg.attach(msg_text)
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=EMAIL_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=TO_EMAIL, msg=msg.as_string())

        print('Notification Sent')


stock_percentage_change = get_stock_percentage_change()
up_down = None
if stock_percentage_change > 5:
    up_down = '🔺'
    send_email(stock_percentage_change, up_down)
elif stock_percentage_change < -5:
    up_down = '🔻'
    send_email(stock_percentage_change, up_down)
