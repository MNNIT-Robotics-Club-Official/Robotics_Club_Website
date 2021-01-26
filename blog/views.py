from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Blog
from .form import BlogForm

# Create your views here.
@login_required
def list(request):
    context={}
    context['bloglist']=Blog.objects.all()
    return render(request,'blog/blog_list.html',context)

@login_required
def detail(request,pk):
    context={}
    context['blog']=Blog.objects.get(pk=pk)
    return render(request,'blog/blog_detail.html',context)

@login_required
def createblog(request):
    context={}
    if request.method=='POST':
        form=BlogForm(request.POST)
        form.instance.author=request.user
        form.save()
        return redirect('blog_list')
    else:
        form=BlogForm()
        context['form']=form
    return render(request,'blog/blog_form.html',context)

@login_required
def deleteblog(request,pk):
    blog=Blog.objects.get(pk=pk)
    if(request.user==blog.author):
        blog.delete()
    return redirect('blog_list')

@login_required
def updateblog(request,pk):
    context={}
    blog = Blog.objects.get(pk=pk)
    if (request.user == blog.author):
        if request.method == "GET":
            form=BlogForm(instance=blog)
            context['form']=form
            return render(request, 'blog/blog_form.html', context)
        else:
            form=BlogForm(request.POST,instance=blog)
            form.instance.author=request.user
            form.save()
        return redirect('blog_detail',pk=blog.pk)
    else:
        return HttpResponse("sorry you dont have permission :)")