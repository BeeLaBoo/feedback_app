from email import message
import smtplib


def send_mail(customer, pattern_name, rating, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = '89844dcc20ad0c'
    password = '8028ebb4800c46'
    


sender = "from@example.com"
receiver = "to@example.com"

message = f"""\
Subject: Hi there! 
To: {receiver}
From: {sender}

This is a feedback message."""

with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
    server.login("89844dcc20ad0c", "8028ebb4800c46")
    server.sendmail(sender, receiver, message)

