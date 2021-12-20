from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from api.serializers import NewsItemSerializer
from news.models import NewsItem
from api.response import Response


class ListItems(ListAPIView):
    serializer_class = NewsItemSerializer
    
    def get_queryset(self):
        queryset = NewsItem.objects.all()

        # search title by text
        query = self.request.query_params.get('q', None)
        if query is not None:
            queryset = queryset.filter(title__icontains=query.lower())
            return queryset

        # filter by type
        type = self.request.query_params.get('type', None)
        if type is not None:
            queryset = queryset.filter(type=type.lower())
            return queryset

        return queryset
    
    def list(self, request):
        '''
        List all news items in the database.
        '''
        queryset = self.get_queryset().order_by('title')
        serializer = self.serializer_class(queryset, many=True)
        return Response(data={'news': serializer.data}, status=status.HTTP_200_OK)
    


class AddItem(APIView):
    
    def post(self, request):
        '''
        Create a news item and persist it to the database.
        '''
        serializer = NewsItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={'news': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(errors=serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UpdateItem(APIView):

    def get(self, request, id):
        '''
        Get news item by ID
        '''

        try:
            news = NewsItem.objects.get(id=id)
            serializer = NewsItemSerializer(news)
            return Response(data={'news': serializer.data}, status=status.HTTP_201_CREATED)
        except:
            return Response(errors={'message': 'News Item does not exist'}, status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, id):
        '''
        modify news item if and only if it was not added from Hacker News server
        '''
        
        try:
            news_item = NewsItem.objects.get(is_from_api=False, id=id)
        except:
            return Response(errors={'message': 'Cannot modify news item from Hacker News API'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = NewsItemSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.instance = news_item
            serializer.save()
            return Response(data={'news': serializer.data}, status=status.HTTP_200_OK)
        return Response(errors=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        '''
        Delete news item if and only if it was not added from Hacker News server
        '''
        
        try:
            news_item = NewsItem.objects.get(is_from_api=False, id=id)
            news_item.delete()
            return Response(data={'news': {}}, status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(errors={'message': 'Cannot delete news item from Hacker News API'}, status=status.HTTP_400_BAD_REQUEST)
