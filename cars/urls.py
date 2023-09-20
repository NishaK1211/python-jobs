# cars/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
]