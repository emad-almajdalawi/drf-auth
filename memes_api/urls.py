from django.urls import path
from .views import MemesListCreateAPI, MemesDetailUpdateDeleteAPI

urlpatterns = [
    path('api/memes-list', MemesListCreateAPI.as_view(), name='memes-list'),
    path('api/<int:pk>', MemesDetailUpdateDeleteAPI.as_view(), name='memes-detail'),
]