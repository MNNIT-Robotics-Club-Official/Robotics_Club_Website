from django.urls import path
from project import views

app_name = 'project'

urlpatterns=[
    path('',views.list,name='list'),
    path('detail/<int:pk>/',views.detail,name='detail'),
    path('overview/<int:pk>/', views.overview, name='overview'),
    path('delete/<int:pk>/',views.delete,name='delete'),
    path('create/',views.create,name='create'),
    path('update/<int:pk>/',views.update,name='update'),
    path('access/<key>/',views.sharedPage,name='sharedPage'),
    path('createlink/<int:pk>/',views.createShare,name='createLink'),
    path('filter=<slug:tag>/',views.filter,name='filter'),
]