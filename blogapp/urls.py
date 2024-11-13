from django import views
from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('add/', views.add_blog_post, name='add_blog_post'),
    path('edit/<int:pk>/', views.edit_blog_post, name='edit_blog_post'),
    path('view/', views.view_blog_posts, name='view_blog_posts'),
    
]


