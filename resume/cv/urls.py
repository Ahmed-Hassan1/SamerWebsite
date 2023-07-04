from django.urls import path
from .views import *


urlpatterns = [
    path('',homePage,name="home"),
    path('work/',workPage,name="work"),
]