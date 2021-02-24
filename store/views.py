from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'store/home.html')

def library(request):
    return render(request, 'store/library.html')

def contact(request):
    return render(request, 'store/contact.html')