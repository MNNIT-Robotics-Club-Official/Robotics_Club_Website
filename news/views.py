from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import NewsForm
from .models import News
from django.contrib import messages
from RoboClub.decorators import has_role_head_or_coordinator
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.core.mail import EmailMessage,send_mass_mail
from django.conf.global_settings import EMAIL_HOST_USER
from django.utils import timezone
from django.http import JsonResponse
import threading
from threading import Thread
# Create your views here.
class EmailThread(threading.Thread):
    def __init__(self, subject, html_content, recipient_list):
        self.subject = subject
        self.recipient_list = recipient_list
        self.html_content = html_content
        threading.Thread.__init__(self)

    def run (self):
        msg = EmailMessage(self.subject, self.html_content, EMAIL_HOST_USER, self.recipient_list)
        msg.content_subtype = "html"
        msg.send()

def news(request):
    context={}
    context['newslist']=News.objects.filter(is_open=True).order_by('-pk')
    context['newslistall'] = News.objects.all().order_by('-pk')
    return render(request,"news/notice.html",context)

@login_required
def collegenews(request):
    context = {}
    context['newslist'] = News.objects.filter(is_open=False).order_by('-pk')
    return render(request, "news/notice_college.html", context)

@has_role_head_or_coordinator
def createNews(request):
    context={}
    if request.method=='POST':
        form=NewsForm(request.POST)
        form.save()
        return redirect('news:news_page')
    else:
        form=NewsForm()
        context['form']=form
    return render(request,'news/notice_form.html',context)

@has_role_head_or_coordinator
def broadCastNews(request,pk):
    # news_id=request.POST.get('id')
    news = News.objects.get(id=pk)
    if not news.allow_broadcast():
        messages.success(request, f"Broadcast for this post has been recently done,try again after 5 minutes")
        return redirect('news:news_page')
    mail_subject = news.title
    notice_body = render_to_string('news/notice_email.html', context={'body': news.content})
    to_users = []
    for user in User.objects.all():
        if user.is_active and user.email is not EMAIL_HOST_USER:
            to_users.append(user.email)
    try:
        for i in range(0,len(to_users),100):
            EmailThread(mail_subject, notice_body, to_users[i:i+100]).start()
        messages.success(request, f'Notice has been broadcast to all users')
        news.broadcast=timezone.now()
        news.save()
    except:
        messages.success(request, f'Notice was not broad casted')
    return redirect('news:news_page')

@has_role_head_or_coordinator
def deleteNews(request,pk):
    news=News.objects.get(pk=pk)
    if(request.user.profile.role >1):
        news.delete()
    return redirect('news:news_page')

@has_role_head_or_coordinator
def updateNews(request,pk):
    context={}
    news = News.objects.get(pk=pk)
    if (request.user.profile.role >1):
        if request.method == "GET":
            form=NewsForm(instance=news)
            context['form']=form
            return render(request, 'news/notice_form.html', context)
        else:
            form=NewsForm(request.POST,instance=news)
            form.save()
        return redirect('news:news_page')
    else:
        messages.info(request,"Sorry you dont have permission")
        return redirect('news:news_page')

