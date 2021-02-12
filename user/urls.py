from django.urls import path
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
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
]