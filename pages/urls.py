from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('community/', views.community, name='community'),
    path('education/', views.education, name='education'),
    path('members/', views.members, name='members'),
]
