from django.urls import path
from .views import home, videos, songs, movies

urlpatterns = [
    path('', home, name='home'),
    path('videos/', videos, name='videos'),
    path('songs/', songs, name='songs'),
    path('movies/', movies, name='movies')
]