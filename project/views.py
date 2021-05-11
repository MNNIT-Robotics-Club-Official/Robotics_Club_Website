from django.shortcuts import render,redirect,HttpResponse
from django.urls import resolve
from django.http import JsonResponse
from project.models import Project,ShareKey
from .forms import ProjectForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string
from RoboClub.decorators import has_role_head_or_coordinator,allow_shares
from django.contrib import messages
# Create your views here.

def list(request):
    context={}
    project_all=Project.objects.get_queryset().order_by('id')
    page=request.GET.get('page')
    paginator=Paginator(project_all,9)
    projects=paginator.get_page(page)
    context['projects'] = projects
    return render(request, 'project/project_list.html', context)

def filter(request,tag) :
    context={}
    project_all=Project.objects.filter(tags__slug__in=[tag])
    page = request.GET.get('page')
    paginator = Paginator(project_all, 9)
    projects = paginator.get_page(page)
    context['projects'] = projects
    return render(request, 'project/project_list.html', context)

def featured(request):
    context={}
    project_all = Project.objects.filter(tags__name__in=['featured']).order_by('id')
    page = request.GET.get('page')
    paginator = Paginator(project_all, 9)
    projects = paginator.get_page(page)
    context['projects'] = projects
    return render(request, 'project/project_list.html', context)

@allow_shares
def detail(request,pk,*args,**kwargs):
    context={}
    context['project']=Project.objects.get(pk=pk)
    tech=Project.objects.filter(pk=pk).values('comp_and_tech')
    for data in tech:
        text = data['comp_and_tech']
        data_list = text.split(',')

    tech_stack = []
    for text in data_list:
        cleaned = text.strip()       # Removing trailing or leading whitespaces
        tech_stack.append(cleaned)

    context['tech'] = tech_stack

    return render(request,'project/project_detail.html',context)

def overview(request,pk):
    context={}
    context['project']=Project.objects.get(pk=pk)
    tech=Project.objects.filter(pk=pk).values('comp_and_tech')
    for data in tech:
        text = data['comp_and_tech']
        data_list = text.split(',')

    tech_stack = []
    for text in data_list:
        cleaned = text.strip()       # Removing trailing or leading whitespaces
        tech_stack.append(cleaned)

    context['tech'] = tech_stack
    return render(request,'project/project_overview.html',context)

@has_role_head_or_coordinator
def delete(request,pk):
    pro=Project.objects.get(pk=pk)
    pro.delete()
    return redirect('project:list')

@has_role_head_or_coordinator
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
        else:
            messages.error(request,"Invalid form!! Please fill all fields correctly")
        return render(request,'project/project_form.html',{'form':form})


@has_role_head_or_coordinator
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
        else:
            messages.error(request,"Invalid form!! Please fill all fields correctly")
            return render(request,'project/project_form.html',{'form':form})
    return HttpResponse("wow")

def sharedPage(request, key):
    try:
        try:
            shareKey = ShareKey.objects.get(pk=key)
        except: raise SharifyError
        # if shareKey.expired: raise SharifyError
        func, args, kwargs = resolve(shareKey.location)
        kwargs["__shared"] = True
        kwargs['pid']=shareKey.project.pk
        return func(request, *args, **kwargs)
    except SharifyError:
        return render(request,'error.html')# or add a more detailed error page. This either means that the key doesn’t exist or is expired

def createShare(request, pk):
    task = Project.objects.get(pk=pk)
    try:
        key = task.sharelink
        key.delete()
        key = ShareKey.objects.create(project=task,pk=get_random_string(40),
                                      expiration_seconds=60*60*24, # 1 day
                                      location = task.get_absolute_url_detail(),
                                      )
    except:
        key = ShareKey.objects.create(project=task, pk=get_random_string(40),
                                      expiration_seconds=60 * 60 * 24,  # 1 day
                                      location=task.get_absolute_url_detail(),
                                      )
    key.save()
    return JsonResponse({"key":key.pk})

class SharifyError(Exception):pass
