from django.shortcuts import render
from .models import Library
import requests

# Create your views here.
def home(request):
    return render(request, 'store/home.html')

def library(request):
    if request.method == "POST":
        movie = Library.objects.get(id=request.POST.get('id'))
        movie.buy_movie()
    library = Library.objects.all()
    count = library.count()
    context = {
        'count': count,
        'library': library,
    }
    return render(request, 'store/library.html', context)

def contact(request):
    data = {
        'method': request.method,
        'title': ''
    }
    if request.method == 'POST':
        data['title'] = request.POST.get('title')
        try:
            contact = Library(
                title=data['title'], 
                director=request.POST.get('director'),
                writer=request.POST.get('writer'),
                description=request.POST.get('description'),
                price=1.99    
            )
            contact.save()
        except e:
            data['error'] = str(e)

    return render(request, 'store/contact.html', data)

def repos(request):
    response = requests.get('https://api.github.com/users/facebook/repos')
    repos = response.json()
    data = {
        'repos': repos
    }
    print(data.keys())
    return render(request, 'store/repos.html', data)