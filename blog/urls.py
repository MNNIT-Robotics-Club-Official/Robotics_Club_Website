from django.urls import path
from . import views

urlpatterns=[
    path('',views.list,name='blog_list'),
    path('detail/<int:pk>/',views.detail,name='blog_detail'),
    #path('detail', views.detail, name='blog_detail'),
    path('form/',views.createblog,name='blog_form'),
    path('delete/<int:pk>/',views.deleteblog,name='blog_delete'),
    path('update/<int:pk>/',views.updateblog,name='blog_update'),
    path('approve/',views.approveblog,name='approve'),
]