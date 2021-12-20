import uuid
from django.db import models

class NewsItem(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    url = models.URLField(blank=True)
    text = models.TextField(blank=True)
    score = models.IntegerField()
    is_from_api = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True)
    added_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
