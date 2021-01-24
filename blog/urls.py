from django.urls import path
from . import views

urlpatterns=[
    path('',views.list,name='blog_list'),
    path('detail/<int:pk>/',views.detail,name='blog_detail'),
    path('form/',views.createblog,name='blog_form')
]