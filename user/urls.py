from django.urls import path
from . import views

app_name = 'user'

urlpatterns=[
    path('',views.userPage,name='user_page'),
    path('login/',views.loginUser,name='login_page'),
    path('register/',views.register,name='register_page'),
]