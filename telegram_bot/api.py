import requests
import json


BASE_URL = 'http://localhost:8000/'

def check_user(username):
    url = f"{BASE_URL}/users/"
    data = {
        'username': username
    }
    
    user = requests.get(url=url, data=data)
    if user.status_code == 200:
        print("All good")
    else:
        print("That user created already enter a new username!")
    print(user.text)



def create_user(username, first_name, password, tg_user_id):
    url = f"{BASE_URL}/users/"
    post_data = {
        'username': username, 
        'first_name': first_name, 
        'password': password,
        'tg_user_id': tg_user_id
    }
    post = requests.post(url=url, data=post_data)
    # print(post)

# create_user("wqerqwewqe", 'eqwwe', 'qwe121231')
