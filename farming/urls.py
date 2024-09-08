from django.urls import path
from . import views

urlpatterns = [
    path("farming/", views.farming, name="farming")
]