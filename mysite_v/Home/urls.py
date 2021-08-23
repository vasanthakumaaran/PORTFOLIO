from django.contrib import admin
from django.urls import path,include
from Home import views


# Django admin header customization

admin.site.site_header = "Developer Vasanth"
admin.site.site_title = "welcome to Dashboard"
admin.site.index_title = "welcome to this portal"
urlpatterns = [  
    #path("", views.nav, name='nav'),
    path("",views.home, name='Home'),
    path('about', views.about, name='About'),
    path('projects', views.projects, name='Projects'),
    path('contact',views.contact, name='Contact'),
    ]
