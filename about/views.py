from django.shortcuts import render

# Create your views here.

def about_content(request):
    """ A view to return the About page. """
    return render(request, 'about/about.html')