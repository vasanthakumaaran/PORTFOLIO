from django.contrib import admin
from django.urls import path,include
from Home import views

urlpatterns = [  
    path("", views.nav, name='nav'),
    path('home',views.home, name='Home'),
    path('about', views.about, name='About'),
    path('projects', views.projects, name='Projects'),
    path('contact',views.contact, name='Contact'),
]
