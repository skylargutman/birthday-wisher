import datetime as dt
import os
import smtplib
from random import choice
import pandas
from my_secrets import my_email, my_password


def get_birthdays(date):
    compare_date = str(date.month) + str(date.day)
    all_birthday_list = pandas.read_csv("data/birthdays.csv")
    date_birthdays = []
    for row in all_birthday_list.to_dict("records"):
        if compare_date == str(row["month"]) + str(row["day"]):
            date_birthdays. append({"name":row["name"], "email":row["email"]})
    return date_birthdays

today = dt.datetime.today()
birthday_list = get_birthdays(today.date())


def format_letter(name):
    letter_templates = []
    for dir_item in os.listdir("letter_templates"):
        if os.path.isfile("letter_templates/" + dir_item):
            with open(f"letter_templates/{dir_item}") as lt:
                letter_templates.append(lt.read())
    return choice(letter_templates).replace("[NAME]", name)


def send_email(to,subject, message):
    conn_email = my_email
    conn_password = my_password
    conn_server = "smtp.gmail.com"
    with smtplib.SMTP(conn_server, 587) as conn:
        conn.starttls()
        conn.login(user=conn_email, password=conn_password)
        conn.sendmail(
            from_addr=conn_email,
            to_addrs=to,
            msg=f"Subject:{subject}\n\n{message}"
        )
        print(f"Sent email to {to}")

if len(birthday_list) > 0 :
    for record in birthday_list:
        letter = format_letter(record["name"])
        send_email(record["email"],
                   f"Happy Birthday {record['name']}",
                   letter)



