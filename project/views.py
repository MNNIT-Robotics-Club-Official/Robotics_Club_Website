from django.shortcuts import render,redirect
from project.models import Project
from .forms import ProjectForm
from django.core.paginator import Paginator
# Create your views here.
def list(request):
    context={}
    project_all=Project.objects.all()
    page=request.GET.get('page')
    paginator=Paginator(project_all,12)
    projects=paginator.get_page(page)
    context['projects'] = projects
    return render(request, 'project/project_list.html', context)

def filter (request,tag) :
    context={}
    context['projects']=Project.objects.filter(tags__name__in=[tag])
    return render(request, 'project/project_list.html', context)

def detail(request,pk):
    context={}
    context['project']=Project.objects.get(pk=pk)
    return render(request,'project/project_detail.html',context)

def delete(request,pk):
    pro=Project.objects.get(pk=pk)
    pro.delete()
    return redirect('project:list')

def update(request,pk):
    context = {}
    pro=Project.objects.get(pk=pk)
    if request.method == 'GET':
        context['form'] = ProjectForm(instance=pro)
        return render(request, 'project/project_form.html', context)
    else:
        form = ProjectForm(request.POST,request.FILES,instance=pro)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.save()
            form.save_m2m()
        return redirect('project:list')

def create(request):
    context={}
    if request.method=='GET':
        context['form']=ProjectForm()
        return render(request,'project/project_form.html',context)
    else:
        form=ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            form.save_m2m()
        return redirect('project:list')
