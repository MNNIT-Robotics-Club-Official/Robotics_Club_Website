from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('alumini/', views.alumini, name='alumini'),
    path('faculty/', views.faculty, name='faculty'),
    path('gallery/', views.gallery, name='gallery'),
    path('avishkar/', views.avishkar, name='avishkar'),
    path('prosang/', views.prosang, name='prosang'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('achievement/', views.achievement, name='achievement'),
    path('permission/', views.permission, name='permission'),
    path('team/', views.team, name='team'),
    path('coordinator/', views.coordinator, name='coordinator'),
    path('sponsor/', views.sponsor, name='sponsor'),
    path('web/', views.web, name='web'),
    path('collaborate/', views.collaborate, name='collaborate'),
    # path('themes/', views.themes, name='themes'),

]