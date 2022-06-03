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
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            author = request.user
            obj.author = author
            form.save()
            messages.success(request, 'Successfully posted Bolg! returning to all blogs page')
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


def detailed_blog_view(request, blog_id):
    """ view selected blog """
    post = get_object_or_404(blog, pk=blog_id)

    template = 'blog/detailed_blog.html'
    context = {
        'post': post
    }
    return render(request, template, context)


def delete_post(request, post_id):
    """ Deletes blog post. """
    get_object_or_404(blog, pk=post_id).delete()
    messages.success(request, 'Your blog post has been successfully Deleted!.')
    return redirect(reverse('blogs'))
