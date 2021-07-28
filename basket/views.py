from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from products.models import Product

# Create your views here.


def view_basket(request):
    """ A view to render the basket contents page """

    return render(request, "basket/basket.html")


def add_to_basket(request, item_id):
    """ Add a quantity of a specific product to the basket """

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    basket = request.session.get('basket', {})

    if size:
        if item_id in list(basket.keys()):
            if size in basket[item_id]['items_by_size'].keys():
                basket[item_id]['items_by_size'][size] += quantity
                messages.success(
                    request, f'You have updated to \
                    {basket[item_id]["items_by_size"][size]} \
                    x {size.upper()}, {product.name}')

            else:
                basket[item_id]['items_by_size'][size] = quantity
                messages.success(
                    request, f'You have added size: {size.upper()}, \
                        {product.name} to your basket.')
        else:
            basket[item_id] = {'items_by_size': {size: quantity}}
            messages.success(
                request, f'You have added Size: {size.upper()}, \
                    {product.name} to your basket.')
    else:
        if item_id in list(basket.keys()):
            basket[item_id] += quantity
            messages.success(
                request, f'You have updated {product.name} \
                    quantity to {basket[item_id]}.')
        else:
            basket[item_id] = quantity
            messages.success(
                request, f'You have added {product.name} to your basket.')

    request.session['basket'] = basket
    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """ Adjust the quantity of a specific product to the specified amount """

    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    basket = request.session.get('basket', {})

    if size:
        if quantity > 0:
            basket[item_id]['items_by_size'][size] = quantity
        else:
            del basket[item_id]['items_by_size'][size]
            if not basket[item_id]['items_by_size']:
                basket.pop(item_id)
    else:
        if quantity > 0:
            basket[item_id] = quantity
        else:
            basket.pop(item_id)

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_from_bask(request, item_id):
    """ Remove a product from the basket """

    try:
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        basket = request.session.get('basket', {})

        if size:
            del basket[item_id]['items_by_size'][size]
            if not basket[item_id]['items_by_size']:
                basket.pop(item_id)
        else:
            basket.pop(item_id)

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
