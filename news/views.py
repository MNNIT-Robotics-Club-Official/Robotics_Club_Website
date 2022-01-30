from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import NewsForm
from .models import News
from django.contrib import messages
from RoboClub.decorators import has_role_head_or_coordinator
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.http import JsonResponse
# Create your views here.

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
    mail_subject = news.title
    message = render_to_string('news/notice_email.html', context={'body': news.content})
    to_users = []
    for user in User.objects.all():
        try:
            email = EmailMessage(
                subject=mail_subject, body=message,to=[user.email],
            )
            email.content_subtype = "html"
            email.send()
        except:
            pass
    messages.success(request, f'Notice has been broadcasted to all users')
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