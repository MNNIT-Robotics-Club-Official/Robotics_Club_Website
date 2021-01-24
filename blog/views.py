from django.shortcuts import render,redirect,HttpResponse
from .models import Blog
from .form import BlogForm

# Create your views here.
def list(request):
    context={}
    context['bloglist']=Blog.objects.all()
    return render(request,'blog/blog_list.html',context)

def detail(request,pk):
    context={}
    context['blog']=Blog.objects.get(pk=pk)
    return render(request,'blog/blog_detail.html',context)


def createblog(request):
    context={}
    if request.user.is_superuser:
        if request.method=='POST':
            form=BlogForm(request.POST)
            form.save()
            return redirect('blog_list')
        else:
            form=BlogForm()
            context['form']=form
        return render(request,'blog/blog_form.html',context)
    else:
        return HttpResponse("Sorry You don't have permission :)")