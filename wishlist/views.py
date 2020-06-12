from django.shortcuts import render, redirect, reverse

# Create your views here.
def view_wishlist(request):
    """A View that renders the wishlist contents page"""
    return render(request, "wishlist.html")


def add_to_wishlist(request, id):
    """Add a product to the wishlist"""
    wishlist = request.session.get('wishlist', [])
    if id not in wishlist:
        wishlist.append(int(id)) 
    request.session['wishlist'] = wishlist
    print('add wishlist', wishlist)
    return redirect(reverse('index'))


def remove_from_wishlist(request, id):
    """
    Remove a product from wishlist
    """
    wishlist = request.session.get('wishlist', [])
    if int(id) in wishlist:
        wishlist.remove(int(id))    
    request.session['wishlist'] = wishlist
    return redirect(reverse('index'))

def delete_from_wishlist(request, id):
    """
    Remove a product from detailed wishlist view
    """
    wishlist = request.session.get('wishlist', [])
    if int(id) in wishlist:
        wishlist.remove(int(id))    
    request.session['wishlist'] = wishlist
    return redirect(reverse('view_wishlist'))
