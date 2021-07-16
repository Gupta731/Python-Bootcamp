import requests
import os
from twilio.rest import Client

LONGITUDE = 87.3167
LATITUDE = 23.4833
API_ENDPOINT = 'https://api.openweathermap.org/data/2.5/onecall'
API_KEY = os.environ.get("OWM_API_KEY")
account_sid = 'AC471026b76d060900a2a5fce49b267bd8'
auth_token = os.environ.get("AUTH_TOKEN")

will_rain = False
parameters = {
    'lat': LATITUDE,
    'lon': LONGITUDE,
    'units': 'metric',
    'appid': API_KEY,
    'exclude': 'current,minutely,daily'
}

response = requests.get(url=API_ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()['hourly'][:12]

for hour_data in data:
    weather_id = hour_data['weather'][0]['id']
    print(weather_id)
    if weather_id < 700:
        will_rain = True

if will_rain:
    print('Message sent')
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It's going to rain today. Bring an umbrella ☂️",
            from_='+19495418631',
            to='+919609529801'
        )
    print(message.status)
