from ast import Delete
from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('delete/<str:pk>',views.delete,name='delete')
]