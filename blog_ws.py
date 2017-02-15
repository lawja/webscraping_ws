from bs4 import BeautifulSoup
import urllib
import matplotlib.pyplot as plt
import threading
import smtplib
import os

cached_posts = []

def find_new_posts(_cached_posts=cached_posts):
    t = 10

    page = urllib.request.urlopen('http://www.jlawrence.co/tb').read()

    soup = BeautifulSoup(page, "html5lib")

    posts = soup.find_all("div",class_="post")

    cant_send = not(_cached_posts)

    # initialization of email server
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    # initialization of the mail driver
    mail.ehlo()
    mail.starttls()

    senderEmail = ''
    senderPass = ''

    recieverEmail = 'jake.lawrence24@gmail.com'

    mail.login(senderEmail, senderPass)

    for post in posts:
        if(not(post in _cached_posts)):
            _cached_posts.append(post)
            if(not(cant_send)):
                mail.sendmail(senderEmail,recieverEmail,'New post at jlawrence.co/tb')
    threading.Timer(t, find_new_posts).start()

find_new_posts()



