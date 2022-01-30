from django.urls import path
from . import views

app_name = 'news'

urlpatterns=[
    path('',views.news,name='news_page'),
    path('college/',views.collegenews,name='news_college'),
    path('form/',views.createNews,name='news_form'),
    path('delete/<int:pk>/',views.deleteNews,name='news_delete'),
    path('update/<int:pk>/',views.updateNews,name='news_update'),
    path('broadcast/<int:pk>/',views.broadCastNews,name='news_broadcast'),
]