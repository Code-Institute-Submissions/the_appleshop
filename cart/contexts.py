from django.shortcuts import get_object_or_404
from products.models import Product
from .models import Cart


def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering
    every page
    """
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

"""
def make_wishlist_string(cart):
        return ','.join(str(product_id) for product_id in wishlist) 


def make_wishlist_list(productlist):
    if productlist !="":
        tmplist= productlist.split(',')
        tmp_wishlist = [int(product) for product in tmplist]
        return tmp_wishlist
    else:
        return []


def merge_wishlists(tmp_wishlist_from_db, wishlist):
    merged_wishlist = wishlist
    for product in tmp_wishlist_from_db:
        if product not in merged_wishlist:
            merged_wishlist.append(product)
    return merged_wishlist





def get_and_update_cart(request):
    cart = request.session.get('cart', {})
    try:
        user_cart = Cart.objects.get(user=request.user.id)

    except:
        messages.success(request, "Saving cart to database")
        name = str(request.user)+"'s cart"
        product_list = make_wishlist_string(cart)
        user_wishlist = Wishlist(user=request.user, name=name, product_list=product_list)
        user_wishlist.save()


    testcart=[]
    for k,v in cart.items():
        testcart.append((k,v))
    newcart=dict(testcart)
    
"""