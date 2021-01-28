from django.urls import path
from . import views

urlpatterns=[
    path('test/<id>',views.test,name='test'),
    path('list/',views.componentlist,name='component_list'),
    path('add/',views.addcomponent,name='add_component'),
    path('delete/<pk>/',views.deletecomponent,name='delete_component'),
    path('update/<pk>/',views.updatecomponent,name='update_component'),
    path('handle/',views.handlerequest,name='handle_request'),
]