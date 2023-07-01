from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class HomePage(TemplateView):
    template_name='cv/index.html'

class WorkPage(TemplateView):
    template_name='cv/work.html'