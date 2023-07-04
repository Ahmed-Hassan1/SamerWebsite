from django.shortcuts import render
from django.views.generic import TemplateView
from .models import HomeVideo,WorkVideo
# Create your views here.

class HomePage(TemplateView):
    template_name='cv/index.html'


class WorkPage(TemplateView):
    template_name='cv/work.html'


def homePage(request):

    sections=HomeVideo.objects.all()
    context={"sections":sections}
    return render(request,"cv/index.html",context)

def workPage(request):
    videos=WorkVideo.objects.all()
    context={"videos":videos}
    return render(request,"cv/work.html",context)
