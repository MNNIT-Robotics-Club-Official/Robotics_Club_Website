from django.shortcuts import render
from .models import Project

# Create your views here.
def list(request):
    context={}
    context['prolist']=Project.objects.all()
    return render(request,'project/projects.html',context)

def detail(request,pk):
    context={}
    context['project']=Project.objects.get(pk=pk)
    return render(request,'project/projects_detail.html',context)