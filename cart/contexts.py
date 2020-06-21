from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.models import Product
from .models import Cart


def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering
    every page
    """
    if request.user.is_authenticated:
        sync_carts(request)
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0
    product_count = 0
    for id, quantity in cart.items():
        product = get_object_or_404(Product, pk=id)
        total += quantity * product.price
        product_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'product': product})
    return {'cart_items': cart_items, 'total': total, 'product_count': product_count}


def make_cart_strings(cart):
    idstring=""
    quantitystring=""
    for k,v in cart.items():
        idstring+=str(k)+","
        quantitystring+=str(v)+","
    return (idstring, quantitystring)


def make_cart_dict(productstring, quantitystring):

    idlist = productstring.split(',')
    idlist.pop(len(idlist)-1)
    quantitylist = quantitystring.split(',')
    quantitylist.pop(len(quantitylist)-1)
    quantitylist_iter = iter(quantitylist)
    newcart = {}
    for id in idlist:
            newcart[id]=next(quantitylist_iter)
    return newcart


def merge_carts(tmp_cart_from_db, cart):
    merged_cart = cart
    for product in tmp_cart_from_db:
        if product not in merged_cart:
            merged_cart[product]=product[product]
    return merged_cart



@login_required
def sync_carts(request):
    cart = request.session.get('cart', {})
    user_cart = None

    try:
        user_cart = Cart.objects.get(user=request.user.id)

    except:
        messages.success(request, "Saving cart to database")
        name = str(request.user)+"'s cart"
        user_cart = Cart(user=request.user, name=name, product_list="")
        user_cart.save()

    if user_cart.product_list != "":
        if cart == {}:
            request.session['cart'] = make_cart_dict(user_cart.product_list, user_cart.quantity_list)
        else:
            tmp_cart_db=make_cart_dict(user_cart.product_list, user_cart.quantity_list)
            merged_cart = merge_carts(tmp_cart_db, cart)
            tmp_strings = make_cart_strings(merged_cart) 
            user_cart.product_list = tmp_strings[0]
            user_cart.quantity_list = tmp_strings[1]
            user_cart.save()
            request.session['wishlist'] = merged_cart

    elif user_cart.product_list=="": 
        if cart != {}:
            tmp_strings = make_cart_strings(cart) 
            user_cart.product_list = tmp_strings[0]
            user_cart.quantity_list = tmp_strings[1]
            user_cart.save()
    return