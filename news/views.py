from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import NewsForm
from .models import News
from django.contrib import messages
# Create your views here.

def news(request):
    context={}
    context['newslist']=News.objects.all().order_by('-pk')
    return render(request,"news/notice.html",context)

@login_required
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

@login_required
def deleteNews(request,pk):
    news=News.objects.get(pk=pk)
    if(request.user.is_superuser):
        news.delete()
    return redirect('news:news_page')

@login_required
def updateNews(request,pk):
    context={}
    news = News.objects.get(pk=pk)
    if (request.user.is_superuser):
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