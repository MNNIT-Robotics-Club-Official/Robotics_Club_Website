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

def avishkar(request):
    return render(request, 'avishkar.html')

def prosang(request):
    return render(request, 'prosang.html')
    
def donate(request):
    return render(request, 'donate.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def achievement(request):
    return render(request, 'achievement.html')

def components(request):
    return render(request, 'components.html')

def permission(request):
    return render(request, 'permission.html')
  
def workshop(request):
    return render(request, 'workshop.html')
