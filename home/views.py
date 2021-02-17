from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def alumini(request):
    return render(request, 'alumni.html')

def faculty(request):
    return render(request, 'faculty.html')

def gallery(request):
    return render(request, 'gallery.html')

def avishkar(request):
    return render(request, 'avishkar.html')

def prosang(request):
    return render(request, 'prosang.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def achievement(request):
    return render(request, 'achievement.html')

def permission(request):
    return render(request, 'permission.html')
  
def web(request):
    return render(request, 'web.html')
  
def outreach(request):
    return render(request, 'outreach.html')
