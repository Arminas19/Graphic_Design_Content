from django.shortcuts import render
from .models import blog
# Create your views here.


def all_blogs(request):
    """  Blogs """
    blogs = blog.objects.all()

    context = {
        'blogs': blogs,
    }

    return render(request, 'blog/blogs.html', context)


def create_blog(request):
    """  Create blog """   
    return render(request, 'blog/create_blog.html')