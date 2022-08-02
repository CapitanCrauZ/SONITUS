from django.urls import path
from .views import log, register, profile, out

urlpatterns = [
    path('', log, name='login'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('logout/', out, name='logout')
]