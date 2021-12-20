from django.views import View
from django.shortcuts import render 
from django.core.paginator import Paginator

from news.models import NewsItem

class Home(View):
    '''
    View controller for homepage
    '''
    
    def get(self, request):
        news = NewsItem.objects.all().order_by('title')
        paginator = Paginator(news, per_page=7)
        page = request.GET.get('page')
        paged_news = paginator.get_page(page)
        types = None

        context = {
            'news': paged_news,
            'types': types
        }

        # filter news item by type
        if 'type' in request.GET:
            type = request.GET['type']
            if type:
                types = NewsItem.objects.filter(type=type.lower())

                context['types'] = types
    
        return render(request, 'news/home.html', context)
        

class Search(View):
    '''
    View controller for search functionality.
    '''

    def get(self, request):
        context = {}

        # search news title by text
        if 'q' in request.GET:
            query = request.GET['q']
            if query:
                news = NewsItem.objects.filter(title__icontains=query)
                context['news'] = news

        return render(request, 'news/search.html', context)
