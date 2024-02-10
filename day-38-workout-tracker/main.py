import os
import requests

APP_ID = os.environ['APP_ID']
API_KEY = os.environ['API_KEY']

nl_exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

headers = {'x-app-id': APP_ID, 'x-app-key': API_KEY}

user_input = input('Tell me the exercise you did: ')

nl_exercise_parameters = {
    'query': user_input,
    'weight_kg': '81',
    'height_cm': '168',
    'age': '35'
}

r = requests.post(url=nl_exercise_endpoint, json=nl_exercise_parameters, headers=headers)
result = r.json()
print(result)
