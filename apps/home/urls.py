from django.urls import path
from .views import home, videos

urlpatterns = [
    path('', home, name='home'),
    path('videos/', videos, name='videos')
]