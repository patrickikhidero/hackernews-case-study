from django.test import TestCase, Client
from rest_framework import status

from news.models import NewsItem


class TestNews(TestCase):
    
    client = Client()
    BASE_URL = 'http://localhost:8000'

    def test_save_news(self):
        '''
        Test that news items are successfully saved to the database
        '''
        news_item = NewsItem(title='JavaScript and React', author='Ben Idewor', type='story', url='', is_from_api=True, time='34i95892', score='3' )
        news_item.save()
        self.assertEqual(news_item.title, 'JavaScript and React')
        self.assertEqual(news_item.author, 'Ben Idewor')

    def test_views(self):
        '''
        Verify that both home and search pages are displayed when a request reaches their respective routes
        '''
        home = self.client.get(f'{self.BASE_URL}')
        search = self.client.get(f'{self.BASE_URL}/search')
        self.assertEqual(home.status_code, status.HTTP_200_OK)
        self.assertEqual(search.status_code, status.HTTP_200_OK)

    def test_search(self):
        '''
        Test that news title can be searched by text
        '''
        news_item = NewsItem(title='JavaScript and React', author='Ben Idewor', type='story', url='', is_from_api=True, time='34i95892', score='3' )
        news_item.save()
        query = 'React'
        search = self.client.get(f'{self.BASE_URL}?q={query}')

        self.assertTrue(query in news_item.title.split(' '))
        self.assertEqual((search.request['QUERY_STRING']), 'q=React')

    def test_filter(self):
        '''
        Test that news item can be filtered by type
        '''
        news_item = NewsItem(title='JavaScript and React', author='Ben Idewor', type='job', url='', is_from_api=True, time='34i95892', score='3' )
        news_item_2 = NewsItem(title='JavaScript and React', author='Ben Idewor', type='story', url='', is_from_api=True, time='34i95892', score='3' )
        news_item.save()
        news_item_2.save()

        query = 'Job'
        query_2 = 'story'
        filter = self.client.get(f'{self.BASE_URL}?type={query}')
        filter_2 = self.client.get(f'{self.BASE_URL}?type={query_2}')
        
        self.assertEqual(query.lower(), news_item.type)
        self.assertEqual((filter.request['QUERY_STRING']), 'type=Job')
        self.assertEqual(query_2, news_item_2.type)
        self.assertEqual((filter_2.request['QUERY_STRING']), 'type=story')
