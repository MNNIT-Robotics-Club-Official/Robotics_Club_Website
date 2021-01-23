from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('alumni/', views.alumni, name='alumni'),
    path('faculty/', views.faculty, name='faculty'),
    path('gallery/', views.gallery, name='gallery'),
    path('testimonial/', views.testimonial, name='testimonial'),
]