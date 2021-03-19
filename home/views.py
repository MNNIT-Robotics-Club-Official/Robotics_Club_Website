from django.shortcuts import render,redirect
from django.http import JsonResponse
from .forms import ContactForm
from django.core.mail import EmailMessage
from django.contrib import messages
from django.template.loader import render_to_string
from project.models import Project
# Create your views here.
def contact(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        user=form['name'].value()
        email=form['email'].value()
        body=form['body'].value()
        subject=form['subject'].value()
        message = render_to_string('contact_form.html', {
            'user': user,
            'email': email,
            'body':body,
            'subject':subject
        })
        email = EmailMessage(
            subject, message, to=['roboclubmnnit.test@gmail.com']
        )
        email.send()
        # print("yes")
        messages.success(request,'Message sent successfully')
    return JsonResponse({'message':'Form sent successfully'})

def index(request):
    context={}
    context['form']=ContactForm()
    project_all = Project.objects.filter(tags__name__in=['featured']).order_by('id')[:5]
    context['featured'] = project_all
    return render(request, 'index.html',context)

def alumni(request):
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

def spinoff(request):
    return render(request, 'spinoff.html')

def error(request):
    return render(request, 'error.html')

def error_404(request,exception):
    return render(request, 'error.html')

# def themes(request):
#     return render(request, 'index.html#themes')

