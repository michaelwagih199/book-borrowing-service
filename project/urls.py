from django.contrib import admin
from django.urls import path
from django.urls import path, include
from library_app import urls as library_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("library/api/v1/", include(library_urls)),
]
