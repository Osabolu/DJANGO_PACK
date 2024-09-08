
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("Home/", include("farming.urls")),
    path("types/", include("seeds.urls")),
]
