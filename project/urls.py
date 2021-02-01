from django.urls import path
from . import views

app_name = 'project'

urlpatterns=[
    path('',views.list,name='project'),
    #path('detail/<int:pk>',views.detail,name='project_detail'),
    path('details',views.detail,name='project_detail'),
]