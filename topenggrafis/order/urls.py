from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
from django.urls import include

urlpatterns = [
    path('', views.home, name='home'),
    path('order/', views.order, name='order'),
    path('list/', views.list, name='list'),


]