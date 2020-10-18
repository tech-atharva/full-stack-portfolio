from django.urls import path
from Home import views

urlpatterns = [
    path("", views.index),
    path("about/", views.About),
    path("services/", views.Services),
    path("contact/", views.Contact),
]
