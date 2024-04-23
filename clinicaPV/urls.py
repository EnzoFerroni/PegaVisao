from django.urls import path
from clinicaPV.views import index

urlpatterns = [
    path('', index)
]

