from rest_framework.routers import DefaultRouter
from domains.views import DomainViewSet, UserPlanViewSet

router = DefaultRouter()
router.register('domains', DomainViewSet, basename='domains')
router.register('user_plans', UserPlanViewSet, basename="user_plans")

urlpatterns = router.urls

