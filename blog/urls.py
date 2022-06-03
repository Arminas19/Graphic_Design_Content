from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_blogs, name='blogs'),
    path('create/', views.create_blog, name='create_blog'),
    path('<int:blog_id>/', views.detailed_blog_view, name='detailed_blog'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),

]
