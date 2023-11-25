import requests


def signup_test():
    base_url = "http://localhost:8000/auth/signup/"

    user_data = {
        'username': 'testuser8',
        'email': 'testusers@example.com',
        'password1': 'somestrongpass',
        'password2': 'somestrongpass',

    }

    response = requests.post(base_url, data=user_data)

    if response.status_code == 201:
        print("User created successfully.")
        user_id = response.json().get('user_id')
        print(f"User ID: {user_id}")
    elif response.status_code == 400:
        print("Failed to create a user. Validation errors:")
        print(response.json().get('errors'))
    else:
        print("Failed to create a user. Status code:", response.status_code)


import json
from django.core import serializers

def get_transactions():

    base_url = "http://localhost:8000/"
    data = {"token": 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6ImRpbWEifQ.Q9YUkEccrshO6hZ6I_AoIan4w7EuvTKNiR2y8oGtGnk'}
    json_data = json.dumps(data)
    headers = {'Content-Type': 'application/json'}

    response = requests.post(base_url, json_data, headers)
    
    if response.status_code == 200:
        data = response.json()  
        print(data)
    else:
        print("You are not logined", response.status_code)


def create_transaction():

    base_url = "http://localhost:8000/create_transaction/"
    data = {'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6ImRpbWEifQ.Q9YUkEccrshO6hZ6I_AoIan4w7EuvTKNiR2y8oGtGnk',
            'amount': 100.00,
            'date': '2023-11-26',
            'category': 6,
        }
    json_data = json.dumps(data)
    headers = {'Content-Type': 'application/json'}

    response = requests.post(base_url, json_data, headers)
    
    if response.status_code == 201:
        data = response.json()  
        print(data)
    else:
        print("You are not logined", response.status_code)
        print(response.json())
        
        
def get_history_transactions():

    base_url = "http://localhost:8000/history/"
    data = {"token": 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6ImRpbWEifQ.Q9YUkEccrshO6hZ6I_AoIan4w7EuvTKNiR2y8oGtGnk'}
    json_data = json.dumps(data)
    headers = {'Content-Type': 'application/json'}

    response = requests.post(base_url, json_data, headers)
    
    if response.status_code == 200:
        data = response.json()  
        print(data)
        
    else:
        print("You are not logined", response.status_code)
        
        
def search_data():
    base_url = 'http://localhost:8000/search/'
    data = {
        'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6ImRpbWEifQ.Q9YUkEccrshO6hZ6I_AoIan4w7EuvTKNiR2y8oGtGnk',
        'date': '2023-11-26'
    }
    json_data = json.dumps(data)
    
    response = requests.post(base_url, json_data)
    
    print(response.json())



create_transaction()
create_transaction()
get_transactions()