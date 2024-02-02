import smtplib

import password

my_email = 'dannychantesting@gmail.com'
password = 'ighvhaupipfkbxcy'

with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs='dannychantesting@outlook.com',
        msg='Subject:Hello\n\nThis is the body of the email.'
    )