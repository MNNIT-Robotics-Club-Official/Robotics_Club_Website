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
    path('achievement_2016/', views.achievement_2016, name='achievement_2016'),
    path('achievement_2017/', views.achievement_2017, name='achievement_2017'),
    path('achievement_2018/', views.achievement_2018, name='achievement_2018'),
    path('achievement_2019/', views.achievement_2019, name='achievement_2019'),
    path('achievement_2020/', views.achievement_2020, name='achievement_2020'),
    path('achievement_2021/', views.achievement_2021, name='achievement_2021'),
    # path('themes/', views.themes, name='themes'),

]