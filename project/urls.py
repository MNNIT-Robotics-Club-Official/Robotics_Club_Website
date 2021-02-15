from django.urls import path
from project import views

app_name = 'project'

urlpatterns=[
    path('',views.list,name='list'),
    path('detail/<int:pk>/',views.detail,name='detail'),
    # path('details',views.detail,name='project_detai'),
    path('delete/<int:pk>/',views.delete,name='delete'),
    path('create/',views.create,name='create'),
    path('update/<int:pk>/',views.update,name='update'),
    path('filter=<slug:tag>/',views.filter,name='filter'),
]