from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('alumni/', views.alumni, name='alumni'),
    path('faculty/', views.faculty, name='faculty'),
    path('gallery/', views.gallery, name='gallery'),
    path('avishkar/', views.avishkar, name='avishkar'),
    path('prosang/', views.prosang, name='prosang'),
    path('donate/', views.donate, name='donate'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('achievement/', views.achievement, name='achievement'),
]