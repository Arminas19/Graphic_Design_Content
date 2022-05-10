from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_content, name='about'),
    path('contact_success/', views.contact_success, name='contact_success'),
]
