import random
import os
import csv
import datetime as dt
import smtplib

# E-mail account details
my_email = 'dannychantesting@gmail.com'
password = 'ighvhaupipfkbxcy'


def select_random_template(template_path):
    """
    Selects a random email template from the specified directory.

    Args:
        template_path (str): The file path to the directory containing email templates.

    Returns:
        str: The content of a randomly selected email template.
    """
    # List all template files in the directory
    templates = [f for f in os.listdir(template_path) if os.path.isfile(os.path.join(template_path, f))]
    selected_template = random.choice(templates)
    with open(os.path.join(template_path, selected_template), 'r') as file:
        content = file.read()
    return content


# Initialize a dictionary to store birthday information
birthdays_dict = {}

# Read in birthday data from a CSV file
with open('birthdays.csv', newline='') as csvfile:
    # Use DictReader for easy access to columns by header names
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Convert month and day to integers for consistency
        month = int(row['month'])
        day = int(row['day'])
        key = (month, day)
        # Use month and day tuple as key for easy lookup
        if key not in birthdays_dict:
            birthdays_dict[key] = [row]  # Initialize a new list for this key
        else:
            birthdays_dict[key].append(row)  # Append to the existing list

# Determine today's date for matching birthdays
today = (dt.datetime.now().month, dt.datetime.now().day)
recipient_list = {}

# Loop through birthdays to find matches for today
for birthday, row in birthdays_dict.items():
    if birthday == today:
        # Add matching birthdays to recipient list
        for i in row:
            recipient_list[i['name']] = i['email']

# Check if there are any birthdays today
if len(recipient_list) != 0:
    print(recipient_list)
    for recipient, email in recipient_list.items():
        # Select a random email template and replace placeholder with recipient's name
        email_template = select_random_template(template_path='letter_templates')
        email_text = email_template.replace('[NAME]', recipient)

        # Setup SMTP connection for sending the email
        with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
            connection.starttls()  # Upgrade the connection to secure
            connection.login(user=my_email, password=password)  # Login to the email server
            # Send the email
            connection.sendmail(
                from_addr=my_email,
                to_addrs=email,
                msg=f'Subject:Happy Birthday {recipient}!\n\n{email_text}'
            )

            # Print message once email is sent
            print(f'Email sent to {recipient}.\n')

else:
    # Print message if no birthdays today
    print(f'There are no birthdays today.')
