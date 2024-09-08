from django.urls import path
from . import views

urlpatterns = [
    path("seeds/", views.seeds, name="seeds")
]