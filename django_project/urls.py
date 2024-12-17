from django.contrib import admin
from django.urls import path, include 
from django.views.generic.base import TemplateView 

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
]
