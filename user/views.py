from django.shortcuts import render, redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from component.models import Request
from django.template.loader import render_to_string
from django.http import JsonResponse
from .models import Profile
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('user:login_page')
        else:
            # messages.info(request, "Invalid Registration")
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
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
