## Send Motivational Emails on Mondays

import smtplib
import datetime as dt
from auth import *
from random import choice

with open("quotes.txt") as quote_file:
    quotes = quote_file.readlines()

if dt.datetime.now().weekday() == 2:
    try:
        today_quote = choice(quotes)
        quotes.remove(today_quote)
    except IndexError:
        today_quote = "I'm all out of Quotes, time to reload me!"
    finally:
        with smtplib.SMTP(mail_server, port=587) as connection:
            connection.starttls()
            connection.login(user=mail, password=passwd)
            connection.sendmail(
                from_addr=mail,
                to_addrs="josh_miller79@outlook.com",
                msg=f"Subject:Monday Motivator\n\nToday's Motivational Quote:\n\n{today_quote}")


