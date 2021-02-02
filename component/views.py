from django.shortcuts import render,HttpResponse,redirect
from .models import Component,Request
from .forms import ComponenentForm,UpdateComponentForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.http import JsonResponse
# Create your views here.
def test(request,id):
    context={}
    component = Request.objects.filter(component_id=id).filter(status=0)
    othcomp = Request.objects.filter(component_id=id).filter(status=1)
    context['request'] = component
    context['approved']= othcomp
    return render(request,'component/test.html',context)

def componentlist(request):
    context = {}
    if request.is_ajax():
        id=request.GET.get('id')
        component=Request.objects.filter(component_id=id).filter(status=0)
        context['component'] = component
    context['components'] = Component.objects.all()
    return render(request, 'component/component_list.html', context)

def addcomponent(request):
    context = {}
    if request.user.is_superuser:
        if request.method == 'POST':
            form = ComponenentForm(request.POST)
            form.save()
            return redirect('component_list')
        else:
            form = ComponenentForm()
            context['form'] = form
        return render(request, 'component/component_form.html', context)
    else:
        return HttpResponse("Sorry You don't have permission :)")

def deletecomponent(request,pk):
    component=Component.objects.get(pk=pk)
    component.delete()
    return redirect('component_list')

def updatecomponent(request,pk):
    component=Component.objects.get(pk=pk)
    context = {}
    if request.user.is_superuser:
        if request.method == 'POST':
            form = UpdateComponentForm(request.POST,instance=component)
            form.save()
            return redirect('component_list')
        else:
            form = UpdateComponentForm(instance=component)
            context['form'] = form
        return render(request, 'component/component_form.html', context)
    else:
        return HttpResponse("Sorry You don't have permission :)")

def handlerequest(request):
    context={}
    cid=request.GET.get('id')
    user=request.GET.get('user')
    type=request.GET.get('r_type')
    comp = Component.objects.get(pk=cid)  # getting object of group
    user = User.objects.get(username__exact=user)
    req = Request.objects.get(request_user=user, component=comp)
    if type=='0': #approve
        req.status = 1
        req.save()
    elif type=='1': #reject
        req.status=2
        req.delete()
    else:
        print("this should not be happening")
    context['request'] = Request.objects.filter(component=comp).filter(status=0)
    context['approved'] = Request.objects.filter(component=comp).filter(status=1)
    if request.is_ajax():
        html = render_to_string('Component/test_part.html', context, request=request)
        return JsonResponse({'html':html},status=200)
    else:
        return HttpResponse("This is unexpected :(")

def createrequest(request):

    return HttpResponse("Sorry You don't have permission :)")
