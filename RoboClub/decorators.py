from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


def has_role_head(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.profile.role == 3:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('home:permission')
        else:
            return redirect('user:login_page')

    return wrapper_func


def has_role_head_or_coordinator(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.profile.role >= 2:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('home:permission')
        else:
            return redirect('user:login_page')

    return wrapper_func


def is_banned(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.profile.role != 0:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('home:permission')
        else:
            return redirect('user:login_page')

    return wrapper_func
