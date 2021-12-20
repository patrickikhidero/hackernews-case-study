from django.urls import path

from news.views import Home
from news.views import Search

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('search', Search.as_view(), name='search_news')
]
