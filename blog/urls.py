from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_blogs, name='blogs'),
    path('create/', views.create_blog, name='create_blog'),
    path('view/', views.detailed_blog_view, name='detailed_blog'),
]
