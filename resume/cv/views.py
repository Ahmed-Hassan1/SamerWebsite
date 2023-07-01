from django.shortcuts import render
from django.views.generic import TemplateView
from .models import HomeVideo
# Create your views here.

class HomePage(TemplateView):
    template_name='cv/index.html'


class WorkPage(TemplateView):
    template_name='cv/work.html'


def homePage(request):

    sections=HomeVideo.objects.all()
    print(sections)
    context={"sections":sections}
    return render(request,"cv/index.html",context)