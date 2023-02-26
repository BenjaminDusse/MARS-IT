import datetime
from datetime import timedelta

def custom_jwt_payload_handler(user):
    payload = custom_jwt_payload_handler(user)
    payload['exp'] = datetime.utcnow() + timedelta(days=1)
    return payload

# # from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

class CustomJWTAuthentication(JWTTokenUserAuthentication):
    def get_payload(self, user):
        payload = super().get_payload(user)
        payload['chat_id'] = user.contact.chat_id
        return payload


