from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from news.models import NewsItem


class TestAPI(APITestCase):
    BASE_URL = 'http://localhost:8000/api/v1'
    client = APIClient()

    def test_get_all_news_items(self):
        '''
        Test that clients can retrieve all news_items in database
        '''
        news = self.client.get(f'{self.BASE_URL}/news/')
        self.assertEqual(news.status_code, status.HTTP_200_OK)

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

    def test_create_news_item(self):
        '''
        Test that a news item is created
        '''
        payload = {
            "id": "b9bb893c-92f3-4ce6-acb6-ce28a357b3ab",
            "title": "How to walk across a parking lot (2011)",
            "author": "baobaba",
            "type": "story",
            "url": "https://www.raptitude.com/2011/09/how-to-walk-across-a-parking-lot/",
            "text": "",
            "score": 2
        }

        news = self.client.post(f'{self.BASE_URL}/add-news', payload)
        self.assertEqual(news.status_code, status.HTTP_201_CREATED)
