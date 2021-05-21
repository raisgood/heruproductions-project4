from django.shortcuts import render
from .models import Library
import requests

# Create your views here.
def home(request):
    return render(request, 'store/home.html')

def library(request):
    if request.method == "POST":
        movie = Library.objects.get(id=request.POST.get('title'))
        movie.buy_movie()
    library = Library.objects.all()
    count = library.count()
    context = {
        'count': count,
        'library': library,
    }
    return render(request, 'store/library.html', context)

def contact(request):
    return render(request, 'store/contact.html')

def wishlist(request):
    data = {
        'method': request.method,
        'title': ''
    }
    if request.method == 'POST':
        data['title'] = request.POST.get('title')
        data['director'] = request.POST.get('director') 
        data['writer'] = request.POST.get('writer')
        data['description'] = request.POST.get('description')
        try:
            wishlist = Library(
                title=data['title'], 
                director=data['director'],
                writer=data['writer'],
                description=data['description'],    
            )
            wishlist.save()
        except Exception as err:
            data['error'] = 'an error occurred: ' + str(err)

    return render(request, 'store/wishlist.html', data)

def repos(request):
    response = requests.get('https://api.github.com/users/facebook/repos')
    repos = response.json()
    data = {
        'repos': repos
    }
    print(data.keys())
    return render(request, 'store/repos.html', data)