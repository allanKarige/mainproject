from django.shortcuts import render, redirect
from .form import followers_form
from .models import followers


def home_page(request):
    form = followers_form()
    return render(request, 'portfolio/index.html', {'form': form})


def insert_follower(request):
    if request.method == 'POST':
        form = followers_form(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            follower = followers(name=name, email=email)
            follower.save()
            return redirect('home')
    else:
        return redirect('home')


def get_about(request):
    return render(request, 'portfolio/about.html')