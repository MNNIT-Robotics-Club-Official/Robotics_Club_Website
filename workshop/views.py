from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
from .models import Workshop
from .forms import WorkshopForm
from RoboClub.decorators import has_role_head_or_coordinator


# Create your views here.

def workshop(request):
    context = {}
    context['upcoming'] = Workshop.objects.filter(status=1).order_by('-pk')
    context['past'] = Workshop.objects.filter(status=0).order_by('-pk')
    return render(request, "workshop/workshop.html", context)


@has_role_head_or_coordinator
def workshop_form(request):
    context = {}
    if request.method == 'POST':
        form = WorkshopForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('workshop:workshop_page')
        else:
            messages.error(request, "Invalid Input!! Please fill correctly")
            return render(request, "workshop/workshop_form.html", {'form': form})
            # return redirect('workshop:workshop_form')
    else:
        context['form'] = WorkshopForm()
        return render(request, "workshop/workshop_form.html", context)


@has_role_head_or_coordinator
def deleteWorkshop(request, pk):
    workshop = Workshop.objects.get(pk=pk)
    workshop.delete()
    return redirect('workshop:workshop_page')


@has_role_head_or_coordinator
def updateWorkshop(request, pk):
    context = {}
    workshop = Workshop.objects.get(pk=pk)
    if request.method == "GET":
        form = WorkshopForm(instance=workshop)
        context['form'] = form
        return render(request, 'workshop/workshop_form.html', context)
    else:
        form = WorkshopForm(request.POST, request.FILES, instance=workshop)
        if form.is_valid():
            form.save()
            return redirect('workshop:workshop_page')
        else:
            messages.error(request, "Invalid Input!!, Please fill correctly")
            return render(request, 'workshop/workshop_form.html', {'form': form})
