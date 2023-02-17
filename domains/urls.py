from rest_framework.routers import DefaultRouter
from domains.views import DomainViewSet

router = DefaultRouter()
router.register('domains', DomainViewSet, basename='domains')
urlpatterns = router.urls

