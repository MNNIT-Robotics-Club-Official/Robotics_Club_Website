from django.shortcuts import render,HttpResponse,redirect
from .models import Component
from .forms import ComponenentForm,UpdateComponentForm
# Create your views here.
def test(request):
    context={}
    context['comp']=Component.objects.all()
    return render(request,'component/test.html',context)

def addcomponent(request):
    context = {}
    if request.user.is_superuser:
        if request.method == 'POST':
            form = ComponenentForm(request.POST)
            form.save()
            return redirect('test')
        else:
            form = ComponenentForm()
            context['form'] = form
        return render(request, 'component/component_form.html', context)
    else:
        return HttpResponse("Sorry You don't have permission :)")

def deletecomponent(request,pk):
    component=Component.objects.get(pk=pk)
    component.delete()
    return redirect('test')

def updatecomponent(request,pk):
    component=Component.objects.get(pk=pk)
    context = {}
    if request.user.is_superuser:
        if request.method == 'POST':
            form = UpdateComponentForm(request.POST,instance=component)
            form.save()
            return redirect('test')
        else:
            form = UpdateComponentForm(instance=component)
            context['form'] = form
        return render(request, 'component/component_form.html', context)
    else:
        return HttpResponse("Sorry You don't have permission :)")