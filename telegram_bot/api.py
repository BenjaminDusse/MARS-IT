import requests
import json

UZ = 'UZ', ('Uzbek')


BASE_URL = 'http://localhost:8000'

def create_user(tg_user_id, chat_id, lang='uz'):
    post_data = {
        'tg_user_id': tg_user_id,
        'chat_id': chat_id,
        'lang': lang
    }
    # url ga ?tg_user_id laga qoshib jonatishim kerak :D
    url = f"{BASE_URL}/contacts/"
    post = requests.post(url=url, data=post_data)
    print(post)

