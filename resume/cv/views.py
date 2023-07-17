from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
# Create your views here.

class HomePage(TemplateView):
    template_name='cv/index.html'


class WorkPage(TemplateView):
    template_name='cv/work.html'


def homePage(request):

    sections=HomeVideo.objects.all()

    header=AboutMeHeader.objects.all()
    pgs=AboutMeParagrapgh.objects.all()

    social=SocialMedia.objects.all()

    contact=Contact.objects.all()

    context={"sections":sections,"header":header,"pgs":pgs,"social":social,"contact":contact}
    return render(request,"cv/index.html",context)

def workPage(request):
    videos=WorkVideo.objects.all()
    context={"videos":videos}
    return render(request,"cv/work.html",context)
