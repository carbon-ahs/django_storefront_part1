from django.urls import path
from . import views

# from .views import say_hello

urlpatterns = [
    path("", views.say_hello, name="hlw"),
]
