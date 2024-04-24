from django.urls import path
from clinicaPV.views import index, sobre

urlpatterns = [
    path('', index, name='home',),
    path('sobre/', sobre, name='sobre',),
]

