from django.shortcuts import get_object_or_404
from products.models import Product
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Wishlist




def wishlist_contents(request):
    """
    Ensures that the wishlist contents are available when rendering
    every page
    """
    wishlist = request.session.get('wishlist', [])
    wishlist_items = []

    for id in wishlist:
        product = get_object_or_404(Product, pk=id)
        wishlist_items.append({'product': product})
    
    return {'wishlist': wishlist, 'wishlist_items': wishlist_items}


#@login_required
# def save_wishlist_to_db(request):
#     if request.user.is_authenticated:
#         wishlist = request.session.get('wishlist', [])
#         name = str(request.user)+"'s wishlist"
#         wishlist_store = Wishlist(name=name, user=request.user, products=wishlist)
#         wishlist_store.save()
#         return {'wishlist': wishlist}
