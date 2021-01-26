from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def alumni(request):
    return render(request, 'alumni.html')

def faculty(request):
    return render(request, 'faculty.html')

def gallery(request):
    return render(request, 'gallery.html')

def donate(request):
    return render(request, 'donate.html')

def testimonial(request):
    return render(request, 'testimonial.html')