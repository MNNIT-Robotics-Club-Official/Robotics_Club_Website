from django.shortcuts import render, redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserProfileForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from component.models import Request
from django.template.loader import render_to_string
from django.http import JsonResponse
from component.models import Request
from blog.models import Blog
from project.models import Project
from component.models import Component,Request
from .models import Profile
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request, f'Congratulations {username}!! Your account has been created!')
            return redirect('home:index')
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
            return redirect('user:register_page')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home:index')
        else:
            messages.info(request,"Username or Password is incorrect")

    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect('home:index')

def userPage(request):
    return redirect('user:login_page')


def changerole(request):
    context = {}
    context['heads'] = User.objects.filter(profile__role=3)
    context['coordis'] = User.objects.filter(profile__role=2)
    context['members'] = User.objects.filter(profile__role=1)
    if request.method=='POST':
        type=request.POST.get('r_type')
        uid=request.POST.get('user')
        user=User.objects.get(pk=uid)
        if type=='0':
            user.profile.role=user.profile.role+1
        else:
            user.profile.role=user.profile.role-1
        user.profile.save()
        if request.is_ajax():
            html = render_to_string('user/user_list.html', context, request=request)
            return JsonResponse({'html': html})
    else:
        return render(request,'user/role_change.html',context)

def comprequest(request):
    context={}
    prequests=Request.objects.filter(request_user=request.user).filter(status=0)
    arequests=Request.objects.filter(request_user=request.user).filter(status=1)
    context['prequests']=prequests
    context['arequests']=arequests
    if request.method=='POST':
        cid=request.POST.get('id')
        req=Request.objects.get(component_id=cid,request_user=request.user)
        req.accepted_by_user()
    return render(request, 'user/comp_request.html', context)

def adminPage(request):
    context={}
    context['requests']=Request.objects.filter(status=0)
    context['blogs']=Blog.objects.filter(approved=False)
    return render(request, 'user/admin_dashboard.html', context)

def userProfileCreation(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST,instance=profile)
        if form.is_valid():
            profile.save()
            messages.success(request, f'Your Profile has been updated')
            return redirect('user:profile_page')        
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
            return redirect('user:profile_form')
    else:
        form = UserProfileForm()
    return render(request, 'user/profile_form.html', {'form': form})

@login_required
def userProfile(request):
    context = {}
    context['blogs'] = Blog.objects.filter(author=request.user).order_by('approved')
    context['projects'] = Project.objects.filter(members=request.user).order_by('status')
    context['components'] = Request.objects.filter(request_user=request.user).order_by('status')
    return render(request,'user/user_dashboard.html',context)