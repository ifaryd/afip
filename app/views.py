from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def propos(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'services.html')