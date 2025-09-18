import random
import smtplib
from gc import set_debug

my_email = "phillip.dev.ops@gmail.com"
password = "pmvo zpmq csqe ihlq"
#message = """From: Me <phillip.dev.ops@gmail.com>
#To: Me <ant9499@comcast.net>
#Subject: SMTP email example
#
#
#This is a test message.
#"""

#with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
#    connection.starttls()
#    connection.login(user=my_email, password=password)
#    connection.sendmail(from_addr=my_email,to_addrs=["ant9499@comcast.net"], msg=message)

import datetime as dt
import pandas

#now = dt.datetime.now()
#print(now.year)

#date_of_birth = dt.datetime(year=1974,month=12,day=9)
#print(date_of_birth)

with open("quotes.txt","r") as file:
    quotes = file.readlines()

quote_of_the_day = random.choice(quotes)

now = dt.datetime.now()
if now.weekday() == 3:

    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="ant9499@comcast.net",
            msg=f"Subject:Quote of the Day\n\n{quote_of_the_day}")

#print(quote_of_the_day)