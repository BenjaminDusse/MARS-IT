import requests
import json

UZ = 'UZ', ('Uzbek')


BASE_URL = 'http://localhost:8000'

def create_user(tg_user_id, chat_id, lang='uz'):
    url = f"{BASE_URL}/users/"
    post_data = {
        'tg_user_id': tg_user_id,
        'chat_id': chat_id,
        'lang': lang
    }
    post = requests.post(url=url, data=post_data)
    print(post)

create_user('123123123', '12312323')
