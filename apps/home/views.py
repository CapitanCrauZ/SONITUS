from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home/main/main.html')

def videos(request):
    return render(request, 'home/videos/videos.html')

def songs(request):
    return render(request, 'home/songs/songs.html')

def movies(request):
    return render(request, 'home/movies/movies.html')