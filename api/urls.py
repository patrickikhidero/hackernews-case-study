from django.urls import path

from api.views import ListItems
from api.views import AddItem, UpdateItem


urlpatterns = [
    path('news/', ListItems.as_view(), name='list-items'),
    path('news/<id>', UpdateItem.as_view(), name='update-item'),
    path('add-news', AddItem.as_view(), name='add-item'),
]
