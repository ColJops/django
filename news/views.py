from django.shortcuts import render
from django.template import RequestContext
from .models import *

# Create your views here.

def index(request):
    news = News.objects.all().order_by('-id')
    return render(request, 'news/index.html', {'news': news})
