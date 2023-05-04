from . import views
from django.urls import path

urlpatterns = [
    path('', views.homepage, name='home'),
    path('apps/', views.applications, name='apps'),
    path('contacts/', views.contact, name='contacts'),
    path('org/', views.org, name='org'),
    path('progr/', views.programs, name='programs'),
    path('school/', views.shcool, name='school'),
    path('profile/', views.prof, name='profile'),
]
