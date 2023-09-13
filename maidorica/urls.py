"""
URL configuration for maidorica project.

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
from django.contrib import admin
from django.urls import path
from app1.views import *
from app2.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration/',registration,name='registration'),
    path('home/',home,name='home'),
    path('home1/',home1,name='home1'),
    path('maid/',maid,name='maid'),
    path('retrive/',retrieve,name='retrive'),
    path('Time_table/',Time_table,name='Time_table'),
    path('user_login/',user_login,name='user_login'),
    path('user_logout/',user_logout,name='user_logout'),
    path('nanny/',nanny,name='nanny'),
    path('maid2/',maid2,name='maid2'),
    path('cook/',cook,name='cook'),
    path('booking/',booking,name='booking'),
    path('About/',About,name='About'),
   
]