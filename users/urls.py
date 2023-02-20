from django.urls import path
from rest_framework.routers import DefaultRouter
from users.views import ContactDetail, ContactViewSet, CustomUserViewSet, UserPlanViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register('users', CustomUserViewSet, basename='users')
router.register('contacts', ContactViewSet, basename="contacts")
router.register('user_plans', UserPlanViewSet, basename="user_plans")

urlpatterns  = [
    path("contacts/<int:chat_id>/", ContactDetail.as_view(), name="contact_detail"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += router.urls

