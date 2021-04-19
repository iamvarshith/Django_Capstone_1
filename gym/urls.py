from django.urls import path
from gym import views

urlpatterns = [
    path('', views.home, name= 'home-gym'),
]
