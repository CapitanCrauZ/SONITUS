from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home/home.html')

def videos(request):
    return render(request, 'videos/videos.html')

def songs(request):
    return render(request, 'songs/songs.html')

def movies(request):
    return render(request, 'movies/movies.html')