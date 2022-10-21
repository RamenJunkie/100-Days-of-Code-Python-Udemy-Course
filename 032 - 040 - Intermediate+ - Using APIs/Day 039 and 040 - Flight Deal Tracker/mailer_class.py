from auth import *
import smtplib

class Mailer():

    def __init__(self):
        pass

    def send_email(self, letter_text):
        with smtplib.SMTP(mail_server, port=587) as connection:
            connection.starttls()
            connection.login(user=mail, password=passwd)
            connection.sendmail(
                from_addr=mail,
                to_addrs=tomail,
                msg=f"{letter_text}"
            )