from rest_framework import serializers

from news.models  import NewsItem


class NewsItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = NewsItem
        fields = ('id', 'title', 'author', 'type', 'url', 'text', 'score', 'is_from_api',)
    
