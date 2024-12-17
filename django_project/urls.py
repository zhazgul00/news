from django.contrib import admin
from django.urls import path, include 
from django.views.generic.base import TemplateView 
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title = 'News',
        description = 'documentation',
        default_version = 'v1',
    ),
    public = True
)
urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("accounts.urls")),
    path("api/", include("apis.urls")), 
    path("api-auth/", include("rest_framework.urls")),
    path("api/dj-rest-auth/", include("dj_rest_auth.urls")), 
    path("api/dj-rest-auth/registration/", include("dj_rest_auth.registration.urls")),
    path("", TemplateView.as_view(template_name="home.html"), name="home"), 
    path("articles/", include("articles.urls")), 
    path("", include("pages.urls")), 
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
