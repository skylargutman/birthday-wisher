import smtplib
import datetime as dt
from random import choice
from my_secrets import my_email, my_password



def send_email(to, subject, message):
    connection_email = my_email
    connection_password = my_password

    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(user=connection_email, password=connection_password)
        connection.sendmail(
            from_addr=connection_email,
            to_addrs=to,
            msg=f"Subject:{subject}\n\n{message}"
        )


if dt.datetime.now().weekday() == 0:
    with open("data/quotes.txt", "r") as quotes_file:
        quotes = quotes_file.readlines()
    quote = choice(quotes)
    send_email(["i@skylargutman.com","skylar@signaturecomputer.com"], "Motivational Quote", quote )
else:
    print("not today")



