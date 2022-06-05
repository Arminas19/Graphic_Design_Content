from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse

from .models import Contact
# Create your views here.


def about_content(request):
    """ A view to return the About page. """
    if request.method == 'POST':
        contact = Contact()

        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact.full_name = full_name
        contact.email = email
        contact.subject = subject
        contact.message = message
        contact.save()
        return redirect(reverse('contact_success'))

    return render(request, 'about/about.html')


def contact_success(request):
    return render(request, 'about/contact_success.html', context=None)
