from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'user'

urlpatterns=[
    path('',views.userPage,name='user_page'),
    path('login/',views.loginUser,name='login_page'),
    path('register/',views.register,name='register_page'),
    path('logout/',views.logoutUser,name='logout_page'),
    path('roles/',views.changerole,name='change_role'),
    path('compreq/',views.comprequest,name='component_request'),
    path('admin/',views.adminPage,name='admin_page'),
    path('profileCreation/',views.userProfileCreation,name='profile_form'),
    path('profile/<user>/',views.userProfile,name='profile_page'),
    path('change_password/',views.changepassword,name='change_password'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    ]
