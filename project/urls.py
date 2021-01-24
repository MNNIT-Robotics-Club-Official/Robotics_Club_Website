from django.urls import path
from . import views

app_name = 'project'

urlpatterns=[
    path('',views.list,name='project_list'),
    path('detail/<int:pk>',views.detail,name='project_detail'),
]