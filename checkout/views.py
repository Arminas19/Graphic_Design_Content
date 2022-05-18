from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm 

# Create your views here.

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, f"There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,

    }

    return render(request, template, context)