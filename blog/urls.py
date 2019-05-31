from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'), #leave blank to make as homepage
    path('about/', views.about, name='blog-about'),
]