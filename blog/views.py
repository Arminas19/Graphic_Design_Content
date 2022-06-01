from django.shortcuts import render

# Create your views here.

def all_blogs(request):
    """  Blogs """
    return render(request, 'blog/blogs.html')