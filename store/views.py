from django.shortcuts import render
from .models import Library

# Create your views here.
def home(request):
    return render(request, 'store/home.html')

def library(request):
    library = Library.objects.all()
    count = library.count()
    context = {
        'count': count,
        'library': library,
    }
    return render(request, 'store/library.html', context)

def contact(request):
    return render(request, 'store/contact.html')