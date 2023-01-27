from domains.telegram_bot import utils

from domains.models import Contact, UZ



def create_user(chat_id, tg_user_id):
    try:
        Contact.objects.create(chat_id=chat_id, tg_user_id=tg_user_id)
    except:
        pass


def get_user(chat_id):
    users = Contact.objects.filter(chat_id=chat_id)
    if not users.exists():
        return None
    return users.first()


def set_user_lang(user, lang):
    user.lang = lang
    user.save()


def get_user_phone_number(phone_number):
    users = Contact.objects.filter(phone_number=phone_number, chat_id__isnull=True, tg_user_id__isnull=True)
    if not users.exists():
        return None
    return users.first()


def set_phone_number(user, phone_number):
    user.phone_number = phone_number
    user.code = "11111"
    user.save()


def set_user_verified(user):
    user.is_verified = True
    user.save()

