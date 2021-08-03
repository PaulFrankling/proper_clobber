from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from basket.contexts import basket_contents

import stripe

def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(
            request, "There's nothing in your basket at the moment!")
        return redirect(reverse('products'))

    current_basket = basket_contents(request)
    total = current_basket['grand_total']
    stripe_total = round(total * 100)

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JK9zxFb44BjYqLVdvvwyLOpCfTHMknzQUsLtiEb24Gvms3Yl10lrX3o8wTrR1LjiCd5Fs8vO7C7TepASK28pwG400ECSD0Q9K',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
