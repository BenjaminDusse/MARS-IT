import requests
import json

UZ = 'UZ', ('Uzbek')
RU = 'RU', ('Russian')


BASE_URL = 'http://127.0.0.1:8000'

async def create_user(chat_id, lang=UZ):
    # url ga ?tg_user_id laga qoshib jonatishim kerak :D
    data = {
        'chat_id': chat_id,
        'lang': lang
    }
    headers = {
        "Accept": 'application/json',
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0",  
    }
    response = requests.post(
        url=f"{BASE_URL}/contacts/",
        json=data,
        headers=headers
    )
    print(response.text)

    print(response.reason)

async def get_user(chat_id):

    response = requests.get(
        url=f"{BASE_URL}/contacts/{chat_id}/"
    )
    print("Getting user")
