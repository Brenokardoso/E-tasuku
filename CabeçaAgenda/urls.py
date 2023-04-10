from django.contrib import admin
from django.urls import path
from .views import home,tarefas,include

urlpatterns = [
    path('',home),
    path('tasks/',tarefas),
    path('recursos',include)
]



