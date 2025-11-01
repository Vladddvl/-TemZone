from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('instruments/', views.instruments, name='instruments'),
    path('news/', views.news, name='news'),
    path('search/', views.search, name='search'),
]