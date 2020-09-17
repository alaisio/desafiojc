'''
from django.urls import path, include
from agendamentos.views import index 

urlpatterns = [
    path('', index)
]

