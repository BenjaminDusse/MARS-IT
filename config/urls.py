from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="Domain Check Project",
        default_version='v1',
        description="This core functionalities of all by Benjamin Dusse",
        contact=openapi.Contact(email="")
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path("", include("users.urls")),
    path('__debug__/', include('debug_toolbar.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]


