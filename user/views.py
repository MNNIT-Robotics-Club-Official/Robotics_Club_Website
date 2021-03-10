from django.shortcuts import render, redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserProfileForm,PasswordResetForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from component.models import Request,Component
from django.template.loader import render_to_string
from django.http import JsonResponse
from blog.models import Blog
from project.models import Project
from django.contrib.auth import get_user_model
from .models import Profile
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from RoboClub.decorators import has_role_head,has_role_head_or_coordinator
# Create your views here.

def register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                to_email = form.cleaned_data.get('email')
                if not to_email.find("@mnnit.ac.in")==-1:
                    user.is_active = False
                    user.save()
                    current_site = get_current_site(request)
                    mail_subject = 'Activate your account.'
                    message = render_to_string('user/acc_active_email.html', {
                        'user': user,
                        'domain': current_site.domain,
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'token': default_token_generator.make_token(user),
                    })
                    email = EmailMessage(
                        mail_subject, message, to=[to_email]
                    )
                    email.send()
                    messages.success(request, f'Please check your email to complete the registration')
                    return redirect('user:login_page')
                else:
                    messages.success(request, f'Kindly enter your gsuite id')
                    return redirect('user:register_page')
            else:
                password1 = form.data['password1']
                password2 = form.data['password2']
                for msg in form.errors.as_data():
                    if msg == 'email':
                        messages.error(request, f"Email Already Exists")
                    else:
                        messages.error(request, f"{form.errors[msg]}")
                    if msg == 'password2' and password1 == password2:
                        messages.error(request, f"Selected password is not strong enough")
                    elif msg == 'password2' and password1 != password2:
                        messages.error(request, f"Password and Confirmation Password do not match")
                        
                return redirect('user:register_page')
        else:
            form = UserRegisterForm()
        return render(request, 'register.html', {'form': form})
    else:
        return redirect('home:index')


def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        cuser = User.objects.filter(username=username)
        if len(cuser)==1:
            if not cuser[0].is_active:
                messages.info(request, "Please Confirm Your Email Id")
            elif user is not None:
                login(request, user)
                return redirect('home:index')
            else:
                messages.info(request,"Incorrect Password")
        else:
            messages.info(request,"Username does not exist")

    return render(request,'login.html')


@login_required
def logoutUser(request):
    logout(request)
    return redirect('home:index')


def userPage(request):
    if request.user.is_authenticated:
        return redirect('home:index')
    else:
        return redirect('user:login_page')


@has_role_head
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
            return JsonResponse({'html': html},status=200)
    else:
        return render(request,'user/role_change.html',context)

def comprequest(request):
    context={}
    components=Request.objects.filter(request_user=request.user)
    context['components']=components
    if request.method=='POST':
        cid=request.POST.get('cid')
        req = Request.objects.get(component_id=cid, request_user=request.user)
        req.accepted_by_user()
        if request.is_ajax():
            html = render_to_string('user/user_comp.html', context, request=request)
            return JsonResponse({'html': html},status=200)
    return HttpResponse('This is not be happening')

@has_role_head_or_coordinator
def adminPage(request):
    context={}
    context['requests']=Request.objects.filter(status=0)
    context['blogs']=Blog.objects.filter(approved=False)
    return render(request, 'user/admin_dashboard.html', context)

@login_required
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
def userProfile(request,user):
    context = {}
    if request.method=='GET':
        context['blogs'] = Blog.objects.filter(author__username=user).filter(approved=True).order_by('approved')
        context['projects'] = Project.objects.filter(members__username=user).order_by('status')
        context['cuser'] = Profile.objects.get(user__username=user)
        if request.user.username ==user:
            context['components'] = Request.objects.filter(request_user=request.user).order_by('status')
            context['blogs'] = Blog.objects.filter(author__username=request.user).order_by('approved')
            context['passform'] = PasswordResetForm()
            context['profileform']= UserProfileForm(instance=request.user.profile)
    else:
        pro=Profile.objects.get(user=request.user)
        form = UserProfileForm(request.POST,instance=pro)
        if form.is_valid():
            form.save()
            messages.success(request,'Profile edited successfully')
        else:
            messages.info(request,'Fill form correctly')
        context['cuser'] = Profile.objects.get(user__username=user)
        html = render_to_string('user/user_dashoard_updatepart.html', context, request=request)
        return JsonResponse({'html': html}, status=200)
    return render(request, 'user/user_dashboard.html', context)

@login_required
def changepassword(request):
    context={}
    if request.method=="POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            if not request.user.check_password(form['current_password'].value()):
                messages.info(request, 'Incorrect Password')
            else:
                if form['new_password_1'].value() != form['new_password_2'].value():
                    messages.info(request, 'Password Mismatch')
                else:
                    request.user.set_password(form['new_password_1'].value())
                    messages.success(request, 'Password Changed Successfully')
        context['cuser']=Profile.objects.get(user=request.user)
        html = render_to_string('user/user_dashoard_updatepart.html',context ,request=request)
        return JsonResponse({'html': html}, status=200)
    else:
        HttpResponse('Something is wrong I can feel it')

def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')
