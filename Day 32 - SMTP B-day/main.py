##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
import datetime as dt
import smtplib

import pandas
import random

my_email = "phillip.dev.ops@gmail.com"
password = "pmvo zpmq csqe ihlq"

def generate_letter(birthday_user):
    letter_num = random.randint(1,3)
    with open(f"letter_templates/letter_{letter_num}.txt") as letter_file:
        message = letter_file.read()
        message = message.replace("[NAME]",birthday_user.name)
        #print(message)
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_user.email,
            msg=f"Subject:Happy Birthday\n\n{message}")


now = dt.datetime.now()
bdays = pandas.read_csv("birthdays.csv")
#print(bdays)
month = now.month
day = now.day

for x in bdays.itertuples():
    #print(x.month)
    if x.month == month and x.day == day:
        generate_letter(x)
        #print(f"{x.name}: Today is your birthday")


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




