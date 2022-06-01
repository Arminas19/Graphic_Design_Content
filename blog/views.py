from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import blog
from .forms import BlogForm

# Create your views here.


def all_blogs(request):
    """  Blogs """

    blogs = blog.objects.all()
    context = {
        'blogs': blogs,
    }

    return render(request, 'blog/blogs.html', context)


@login_required
def create_blog(request):
    """  Create blog """   
    blogs = blog.objects.get(author__id=request.user.id)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blogs)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully posted Bolg!')
            return redirect(reverse('blogs'))
        else:
            messages.error(request, 'Failed to post blog, please ensure the form is valid.')
    else:
        form = BlogForm()
        
    template = 'blog/create_blog.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
