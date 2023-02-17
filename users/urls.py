from django.urls import path
from rest_framework.routers import DefaultRouter
from users.views import ContactDetail, ContactViewSet, CustomUserViewSet, UserPlanViewSet

router = DefaultRouter()
router.register('users', CustomUserViewSet, basename='users')
router.register('contacts', ContactViewSet, basename="contacts")
router.register('user_plans', UserPlanViewSet, basename="user_plans")

urlpatterns  = [
    path("contacts/<int:chat_id>/", ContactDetail.as_view(), name="contact_detail"),
]

urlpatterns += router.urls
