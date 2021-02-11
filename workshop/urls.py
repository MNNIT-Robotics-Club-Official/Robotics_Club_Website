from django.urls import path
from . import views

app_name = 'workshop'

urlpatterns=[
    path('',views.workshop,name='workshop_page'),
    path('form/',views.workshop_form,name='workshop_form'),
    path('delete/<int:pk>/',views.deleteWorkshop,name='workshop_delete'),
    path('update/<int:pk>/',views.updateWorkshop,name='workshop_update'),
]