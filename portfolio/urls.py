from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('about/', views.get_about, name='about'),
    path('insert_follower', views.insert_follower),
]