from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def alumni(request):
    return render(request, 'alumni.html')