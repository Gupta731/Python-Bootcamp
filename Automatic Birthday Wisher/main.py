import datetime as dt
import os
import random
import smtplib
import pandas as pd

MY_EMAIL = 'sourabhmahan@gmail.com'
PASSWORD = 'zbuwesyqvzxdlqfm'

current_date = dt.datetime.now()
today = (current_date.month, current_date.day)

birthday_data = pd.read_csv('birthdays.csv')

for index, row in birthday_data.iterrows():
    if today == (row.month, row.day):
        template_list = os.listdir('letter_templates/')
        random_template = random.choice(template_list)
        os.chdir('letter_templates/')
        with open(random_template) as letter_template:
            letter = letter_template.read().replace('[NAME]', f"{row['name']}")
            os.chdir('..')
        try:
            with smtplib.SMTP('smtp.gmail.com') as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=PASSWORD)
                connection.sendmail(from_addr=MY_EMAIL, to_addrs=f"{row['email']}",
                                    msg=f"From: Saurabh Gupta <{MY_EMAIL}>\n"
                                        f"To: {row['email']}\n"
                                        f"Subject: Happy Birthday\n\n{letter}\n"
                                        f"<sent from my python automated birthday wisher>")
        except Exception as e:
            print('Unable to send email.')
