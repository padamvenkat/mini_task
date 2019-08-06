from .views import api_all
from django.urls import path

urlpatterns=[
    path('all/',api_all)
]