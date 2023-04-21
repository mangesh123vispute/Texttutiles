
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [

path( '',views.index,name='index'),
path('analize',views.analize,name='analize'),
path('contactus',views.contact,name='contactus'),
path('about',views.about,name='about'),
path('web',views.index,name='web'),


]

