import requests
import os
from datetime import datetime

GENDER = "male"
WEIGHT_KG = 70
HEIGHT_CM = 179.83
AGE = 25

APP_ID = os.environ.get('APP_ID')
API_KEY = os.environ.get('API_KEY')
NUTRITIONIX_API_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'
SHEETY_API_ENDPOINT = os.environ.get('SHEETY_API_ENDPOINT')
TODAY_DATE = datetime.now().strftime("%d/%m/%Y")
TIME_NOW = datetime.now().strftime("%X")


nutritionix_headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
    'x-remote-user-id': '0',
}

nutritionix_parameters = {
    'gender': GENDER,
    'weight_kg': WEIGHT_KG,
    'height_cm': HEIGHT_CM,
    'age': AGE,
    'query': input('Tell me which exercises you did: ')
}


nutritionix_response = requests.post(url=NUTRITIONIX_API_ENDPOINT, headers=nutritionix_headers,
                                     json=nutritionix_parameters)
nutritionix_data = nutritionix_response.json()['exercises'][0]

sheety_headers = {
    'Content-Type': 'application/json',
}

sheety_parameters = {
    'workout': {
        'date': TODAY_DATE,
        'time': TIME_NOW,
        'exercise': nutritionix_data['name'].title(),
        'duration': nutritionix_data['duration_min'],
        'calories': nutritionix_data['nf_calories'],

    }
}

sheety_response = requests.post(url=SHEETY_API_ENDPOINT, auth=('GuptaPower', API_KEY),
                                headers=sheety_headers, json=sheety_parameters)
print(sheety_response.text)
