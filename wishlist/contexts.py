from django.shortcuts import get_object_or_404
from products.models import Product


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

