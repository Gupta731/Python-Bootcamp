import os
import requests
from datetime import datetime
from dateutil import tz
import smtplib

MY_LAT = 23.5639871
MY_LONG = 87.2794246
FROM_ZONE = tz.tzutc()
TO_ZONE = tz.tzlocal()
MY_EMAIL = 'sourabhmahan@gmail.com'
PASSWORD = os.environ.get("EMAIL_PASSWORD")


def utc_to_local(utc_date_time):
    utc_date = utc_date_time.split('T')[0]
    utc_time = utc_date_time.split('T')[1].split('+')[0]
    utc_timestamp = utc_date + ' ' + utc_time
    utc_timestamp = datetime.strptime(utc_timestamp, '%Y-%m-%d %H:%M:%S')
    utc_timestamp = utc_timestamp.replace(tzinfo=FROM_ZONE)
    local_timestamp = utc_timestamp.astimezone(TO_ZONE)
    return local_timestamp


def is_iss_overhead():
    response = requests.get(url='http://api.open-notify.org/iss-now.json')
    response.raise_for_status()
    data = response.json()

    longitude = float(data['iss_position']['longitude'])
    latitude = float(data['iss_position']['latitude'])

    if (MY_LAT-5 <= latitude <= MY_LAT + 5) and (MY_LONG - 5 <= longitude <= MY_LONG + 5):
        return True


def is_night():
    parameters = {
        'lat': MY_LAT,
        'lng': MY_LONG,
        'formatted': 0,
    }
    response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise_local = utc_to_local(data['results']['sunrise'])
    sunset_local = utc_to_local(data['results']['sunset'])
    time_now = datetime.now().astimezone(TO_ZONE)

    if sunset_local <= time_now <= sunrise_local:
        return True


if is_iss_overhead() and is_night():
    try:
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL,
                                msg=f"From: Saurabh Gupta <{MY_EMAIL}>\n"
                                    f"To: {MY_EMAIL}\n"
                                    f"Subject: ISS Overhead\n\nThe ISS is above you in the sky.\n"
                                    f"<sent from my python automated ISS tracker>")
            print('Notification Sent')
    except Exception as e:
        print('Unable to send email.')
