from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Create your views here.
def register(request):
    #GET
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(data = request.POST)
        if form.is_valid():
            user_registered = form.save()
            if user_registered is not None:
                login(request, user_registered)
                return redirect('/profile/')
    context = {
        'form': form
    }
    return render(
        request, 
        'cuenta/register.html', 
        context
    )
    #POST
def log(request):
    #GET
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user_loged = authenticate(username = username, password = password)
            if user_loged is not None:
                login(request, user_loged)
                return redirect('profile/')
    context = {
        'form': form
    }
    return render(
        request,
        'cuenta/login.html',
        context
    )
    #POST
def out(request):
    #GET
    logout(request)
    return redirect('/')
    #POST
def profile(request):
    #GET
    if request.user.is_authenticated:
        return render(
            request,
            'cuenta/profile.html'
        )
    return redirect('/')



    
    