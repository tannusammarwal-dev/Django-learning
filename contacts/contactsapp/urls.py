from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path("",views.form,name='form'),
    path('submit/', views.submit, name='submit')
]
