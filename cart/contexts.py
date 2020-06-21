from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
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


def make_cart_string(cart):
        return ','.join(str(product_id) for product_id in cart) 


def make_cart_dict(productlist):
    if productlist !="":
        tmplist= productlist.split(',')
        tmp_wishlist = [int(product) for product in tmplist]
        return tmp_wishlist
    else:
        return []


def merge_carts(tmp_cartdict_from_db, cartdict):
    merged_cartdict = cartdict
    for product in tmp_cartdict_from_db:
        if product not in merged_cartdict:
            merged_cartdict.append(product)
    return merged_cartdict



@login_required
def sync_carts(request):
    cart = request.session.get('cart', {})
    user_cart = None

    try:
        user_cart = Cart.objects.get(user=request.user.id)

    except:
        messages.success(request, "Saving cart to database")
        name = str(request.user)+"'s cart"
        user_wishlist = Wishlist(user=request.user, name=name, product_list="")
        user_wishlist.save()

    if user_cart.product_list!=""
        if cart == {}:
            request.session['cart'] = make_cart_list(user_cart.product_list)
        else:
            tmp_wishlist_db=make_wishlist_list(user_wishlist.product_list)
            merged_wishlist = merge_wishlists(tmp_wishlist_db, wishlist)
            user_wishlist.product_list = make_wishlist_string(merged_wishlist)
            user_wishlist.save()
            request.session['wishlist'] = merged_wishlist

    elif user_cart.product_list=="": 
        if cart != {}:
            user_cart.product_list = make_cart_string(cart) 
            user_cart.save()
    return
    
    testcart=[]
    for k,v in cart.items():
        testcart.append((k,v))
    newcart=dict(testcart)
    



def sync_wishlists(request):
    wishlist = request.session.get('wishlist', [])
    user_wishlist = None
    try:
        user_wishlist = Wishlist.objects.get(user=request.user.id)

    except:
        messages.success(request, "Saving wishlist to database")
        name = str(request.user)+"'s wishlist"
        user_wishlist = Wishlist(user=request.user, name=name, product_list="")
        user_wishlist.save()
    
    if user_wishlist.product_list!="":
        if wishlist == []:
            request.session['wishlist'] = make_wishlist_list(user_wishlist.product_list)

        else:
            tmp_wishlist_db=make_wishlist_list(user_wishlist.product_list)
            merged_wishlist = merge_wishlists(tmp_wishlist_db, wishlist)
            user_wishlist.product_list = make_wishlist_string(merged_wishlist)
            user_wishlist.save()
            request.session['wishlist'] = merged_wishlist

    elif user_wishlist.product_list=="": 
        if wishlist != []:
            user_wishlist.product_list = make_wishlist_string(wishlist) 
            user_wishlist.save()
    return