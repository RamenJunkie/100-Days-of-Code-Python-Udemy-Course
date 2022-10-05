##################### Extra Hard Starting Project ######################
from random import choice
import pandas
import datetime as dt
from auth import *
import smtplib

def send_email(email, letter_text):
    with smtplib.SMTP("outlook.office365.com") as connection:
        connection.starttls()
        connection.login(user=mail, password=passwd)
        connection.sendmail(
            from_addr=mail,
            to_addrs=email,
            msg=f"subject: Happy Birthday!\n\n{letter_text}"
        )

name = "TESTER"

names_list = pandas.read_csv("birthdays.csv")
names_dict = names_list.to_dict(orient="records")

for each in names_dict:
    today = dt.datetime(year=each["year"], month=each["month"], day=each["day"])

    if today.date() == dt.datetime.now().date():
        name = each["name"]
        email = each["email"]
        template_file = "letter_templates/letter_"+ str(choice([1,2,3])) +".txt"
        with open(template_file) as template:
            letter_text = template.readlines()

        letter_text = [line.replace("[NAME]", name) for line in letter_text]
        letter_text = "".join(letter_text)

        send_email(email, letter_text)




