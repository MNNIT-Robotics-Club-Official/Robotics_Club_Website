from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'homepage-testimonial.html')

def alumini(request):
    return render(request, 'alumni.html')

def faculty(request):
    return render(request, 'faculty.html')

def coordinator(request):
    return render(request, 'coordinator.html')

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
  
def team(request):
    return render(request, 'team.html')
  
def sponsor(request):
    return render(request, 'sponsor.html')
  
def web(request):
    return render(request, 'web.html')

def collaborate(request):
    return render(request, 'collaborate.html')

def donate(request):
    return render(request, 'donate.html')

def achievement_2016(request):
    return render(request, 'achievement_2016.html')

def achievement_2017(request):
    return render(request, 'achievement_2017.html')

def achievement_2018(request):
    return render(request, 'achievement_2018.html')

def achievement_2019(request):
    return render(request, 'achievement_2019.html')

def achievement_2020(request):
    return render(request, 'achievement_2020.html')

def achievement_2021(request):
    return render(request, 'achievement_2021.html')

# def themes(request):
#     return render(request, 'index.html#themes')

