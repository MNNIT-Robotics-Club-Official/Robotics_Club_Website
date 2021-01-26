from django.urls import path
from . import views

urlpatterns=[
    path('test/',views.test,name='test'),
    path('add/',views.addcomponent,name='add_component'),
    path('delete/<pk>/',views.deletecomponent,name='delete_component'),
    path('update/<pk>/',views.updatecomponent,name='update_component'),
]