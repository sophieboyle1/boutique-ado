from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51INwjeEp80xM5d3OehEBRk3kYPpPTJDMRV5Q5fHTqOwfVrSEYx0MguRK6hdOFupqb2pRJ2gTYmIgB664IzEXsxkl0055rjE8oh',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
