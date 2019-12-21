from django.urls import path

from mypro.views import login

urlpatterns = [
    path('login/',login),
]