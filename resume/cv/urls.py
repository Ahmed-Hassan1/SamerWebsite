from django.urls import path
from .views import *


urlpatterns = [
    path('',homePage,name="home"),
    path('work/',WorkPage.as_view(),name="work"),
]