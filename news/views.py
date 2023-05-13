from django.shortcuts import render
from django.views.generic.list import ListView
from .models import *

# Create your views here.


def index(request):
    news = News.objects.all().order_by('-id')
    #return render(request, 'news/index.html', {'news': news})
    return ListView.as_view(
                        request,
                        news,
                        paginate_by = 10,
                        extra_context = {},
                        template_name = 'index.html')

def news_by_category(request, slug):
    c = Category.objects.get(slug=slug)
    #news = News.objects.filter(category=c).order_by('-id')
    news = c.news_set.all()
    return ListView.as_view(request,
                       news,
                       paginate_by = 10,
                       extra_content = {'c': c},
                       template_name ='news/news_by_category.html')
