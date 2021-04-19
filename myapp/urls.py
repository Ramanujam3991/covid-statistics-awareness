"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin
from . import views

""" path('hello/', views.hello, name='hello'),"""
urlpatterns = [

    path('',views.index),
    path('addnew',views.addnew),
    path('edit/<Country>', views.edit),
    path('update/<Country>', views.update),
    path('delete/<Country>', views.destroy),
    path('api',views.api),
    path('new_api',views.new_api),
    path('api_edit/<country>', views.api_edit),
    path('api_update/<country>', views.api_update),
    path('api_delete/<country>', views.api_destroy),
]