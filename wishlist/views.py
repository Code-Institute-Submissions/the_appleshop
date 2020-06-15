from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from products.models import Product

# Create your views here.
def view_wishlist(request):
    """A View that renders the wishlist contents page"""
    return render(request, "wishlist.html")


def add_to_wishlist(request, id):
    """Add a product to the wishlist"""
    wishlist = request.session.get('wishlist', [])
    product = get_object_or_404(Product, pk=int(id))
    if int(id) not in wishlist:
        wishlist.append(int(id)) 
        request.session['wishlist'] = wishlist
        messages.success(request, "Product {0} has been added to wishlist".format(product))
    return redirect(reverse('index'))


def remove_from_wishlist(request, id):
    """Remove a product from wishlist"""
    wishlist = request.session.get('wishlist', [])
    product = get_object_or_404(Product, pk=int(id))
    if int(id) in wishlist:
        wishlist.remove(int(id))    
        request.session['wishlist'] = wishlist
        messages.success(request, "Product {0} has been removed from wishlist".format(product))
    if request.method=='GET':
        return redirect(reverse('view_wishlist'))
    elif request.method=='POST':
        return redirect(reverse('index'))

