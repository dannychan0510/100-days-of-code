import random
import datetime as dt
import smtplib

# E-mail account details
my_email = 'dannychantesting@gmail.com'
password = 'ighvhaupipfkbxcy'

# Open quotes.txt and read lines into a list
with open('quotes.txt', 'r') as file:
    quotes = file.readlines()

# Use the random module to randomly pick a quote
quote = random.choice(quotes)

# Check date
today = dt.datetime.now()

# Send email if today is Monday (0)
if today.weekday() == 0:
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs='dannychantesting@outlook.com',
            msg=f'Subject:You can do it!\n\n{quote}'
        )
