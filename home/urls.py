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
    path('donate/', views.donate, name='donate'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('achievement/', views.achievement, name='achievement'),
    path('components/', views.components, name='components'),
    path('user_dashboard/', views.user_dashboard, name='user_dashboard'),
    path('permission/', views.permission, name='permission'),
    path('web/', views.web, name='web'),
    path('outreach/', views.outreach, name='outreach'),
]