import requests
import os

# Load environment variables
SHEETY_USERNAME = os.environ["SHEETY_USERNAME"]
SHEETY_PW = os.environ["SHEETY_PW"]
SHEETY_ENDPOINT = (
    "https://api.sheety.co/2629490a2bce2089b8b8dd37ff5689f3/flightDeals/users"
)

# Get data of current existing users
r = requests.get(url=SHEETY_ENDPOINT, auth=(SHEETY_USERNAME, SHEETY_PW))
r.raise_for_status()
users = r.json()["users"]

# Ask user for details
print("Welcome to Flight Club.")
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
email = input("What is your email? ")

# Add user if not in the list
for user in users:
    if (
        user["firstName"].lower() == first_name.lower()
        and user["lastName"].lower() == last_name
        and user["email"].lower() == email.lower()
    ):
        print("You are already in the Flight Club!")
        break
else:
    new_user = {
        "user": {"firstName": first_name, "lastName": last_name, "email": email}
    }
    response = requests.post(
        url=SHEETY_ENDPOINT, json=new_user, auth=(SHEETY_USERNAME, SHEETY_PW)
    )
    response.raise_for_status()
    print("You how now joined the Flight Club!.")
