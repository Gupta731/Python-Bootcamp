from flask import Flask, render_template, request
from post import Post
import requests
from datetime import datetime
import smtplib


MY_EMAIL = 'YOUR_EMAIL_ID'
PASSWORD = 'YOUR_MAIL_PASSWORD'
TO_EMAIL = 'RECIPIENT_EMAIL_ID'

app = Flask(__name__)

year = datetime.now().year

blog_response = requests.get('https://api.npoint.io/9dd7caeb2182f4cecba1').json()
# https://www.npoint.io/docs/9dd7caeb2182f4cecba1
post_objects = []
for post in blog_response:
    post_obj = Post(post['id'], post["title"], post["subtitle"], post["body"], post["author"], post["date"])
    post_objects.append(post_obj)


@app.route('/')
def home():
    return render_template("index.html", all_posts=post_objects, current_year=year)


@app.route('/about')
def about_page():
    return render_template("about.html", current_year=year)


@app.route('/contact', methods=['POST', 'GET'])
def contact_page():
    if request.method == 'POST':
        data = request.form
        send_mail(data['name'], data['email'], data['phone'], data['message'])
        return render_template("contact.html", current_year=year, msg_sent=True)
    return render_template("contact.html", current_year=year, msg_sent=False)


def send_mail(name, email, phone, message):
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=TO_EMAIL,
                            msg=f"From: Saurabh Gupta <{MY_EMAIL}>\n"
                                f"To: {TO_EMAIL}\n"
                                f"Subject: My Blogs message\n\n"
                                f"Name: {name}\n"
                                f"Email: {email}\n"
                                f"Phone: {phone}\n"
                                f"Message: {message}")
        print('Message sent')


@app.route('/post/<int:num>')
def get_post(num):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == num:
            requested_post = blog_post

    return render_template("post.html", post=requested_post, current_year=year)


if __name__ == "__main__":
    app.run(debug=True)
