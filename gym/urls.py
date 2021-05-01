from django.urls import path
from django.views.generic import TemplateView
from gym.views import CreateView
from . import views

urlpatterns = [
    path('', CreateView.as_view()),

    # path('create', views.home, name='home-gym'),
    path('read', views.ReadView.as_view(), name='read'),
    path('update', views.UpdateView.as_view(), name= 'update'),
    path('update/<int:pk>', views.UpdateView.as_view(), name= 'update'),
    path('delete/<int:pk>', views.DeleteView.as_view(), name='delete'),
    path('delete', views.DeleteView.as_view(), name='delete')

]
