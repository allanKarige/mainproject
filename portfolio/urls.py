from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('insert_follower', views.insert_follower),
]