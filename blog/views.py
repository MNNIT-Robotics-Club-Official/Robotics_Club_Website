from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Blog
from .form import BlogForm
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.contrib import messages

# Create your views here.
@login_required
def list(request):
    context={}
    context['bloglist']=Blog.objects.filter(approved=True)
    return render(request, 'blog/blog_list.html', context)

@login_required
def detail(request,pk):
    context={}
    blog=Blog.objects.get(pk=pk)
    if blog.approved == False:
        if blog.author == request.user or request.user.profile.role>=2:
            pass
        else:
            return HttpResponse("You are not authorised")
    context['blog']=blog
    return render(request, 'blog/blog_detail.html', context)

@login_required
def createblog(request):
    context={}
    if request.method=='POST':
        form=BlogForm(request.POST,request.FILES)
        form.instance.author=request.user
        form.save()
        messages.info(request,"Please Wait for Blog to be approved")
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
            form=BlogForm(request.POST,request.FILES,instance=blog)
            form.instance.author=request.user
            form.instance.approved=False
            form.save()
        return redirect('blog_detail',pk=blog.pk)
    else:
        return HttpResponse("sorry you dont have permission :)")

def approveblog(request):
    if request.user.profile.role > 1:
        pk=request.GET.get('id')
        r_type=request.GET.get('r_type')
        if request.is_ajax():
            blog = Blog.objects.get(pk=pk)
            if r_type=='0':
                blog.approve()
                blog.save()
            else:
                blog.delete()
            context={}
            context['blogs']=Blog.objects.filter(approved=False)
            html = render_to_string('user/admin_blog.html', context, request=request)
            return JsonResponse({'html':html},status=200)
        return redirect('blog_detail',pk=pk)
    else:
        return redirect('home:permission')