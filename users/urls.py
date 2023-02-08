from rest_framework.routers import DefaultRouter
from users.views import ContactViewSet, CustomUserViewSet

router = DefaultRouter()
router.register('users', CustomUserViewSet, basename='users')
router.register('contacts', ContactViewSet, basename="contacts")

urlpatterns = router.urls

