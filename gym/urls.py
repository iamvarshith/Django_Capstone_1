from django.urls import path
from django.views.generic import TemplateView
from gym.views import CreateView
from . import views

urlpatterns = [
    path('', CreateView.as_view()),


    # path('create', views.home, name='home-gym'),
    path('read',views.ReadView.as_view(),name='read'),
    # path('update', views.home, name= 'home-gym'),
    # path('delete', views.home, name= 'home-gym'),
]
