"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from appClients import viewsClients
from appSevices import viewsServices
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', viewsClients.index),
    path('newClients', viewsClients.newClients),
    path('updateClients', viewsClients.updateClients),
    path('searchClients', viewsClients.searchClients),
    path('newSevices', viewsServices.newSevices),
    path('updateServices', viewsServices.updateServices),
    path('searchServices', viewsServices.searchServices),
]
