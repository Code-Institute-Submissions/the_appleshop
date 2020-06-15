from django.shortcuts import get_object_or_404
from products.models import Product
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Wishlist
from django.contrib import messages



def wishlist_contents(request):
    """
    Ensures that the wishlist contents are available when rendering
    every page
    """
    wishlist = request.session.get('wishlist', [])

    if request.user.is_authenticated:
        get_and_update_wishlist(request, wishlist)
    #wishlist = request.session.get('wishlist', [])
    wishlist_items = []
    #request.session['wishlist']=[]
    #wishlist=[]
    for id in wishlist:
        product = get_object_or_404(Product, pk=id)
        wishlist_items.append({'product': product})
    return {'wishlist': wishlist, 'wishlist_items': wishlist_items}


def make_wishlist_string(request, wishlist):
        return ','.join(str(product_id) for product_id in wishlist) 


def make_wishlist_list(request, productlist):
    if productlist !="":
        tmplist= productlist.split(',')
        tmp_wishlist = [int(product) for product in tmplist]
        return tmp_wishlist
    else:
        return []


def merge_wishlists(request, tmp_wishlist_from_db, wishlist):
    merged_wishlist = wishlist
    for product in tmp_wishlist_from_db:
        if product not in merged_wishlist:
            merged_wishlist.append(product)
    return merged_wishlist


#@login_required
def get_and_update_wishlist(request, wishlist):
    user_wishlist = None
    try:
        user_wishlist = Wishlist.objects.get(user=request.user.id)

    except:
        messages.success(request, "Saving wishlist to database")
    
    if user_wishlist == None:
        name = str(request.user)+"'s wishlist"
        product_list = make_wishlist_string(request, wishlist)
        user_wishlist = Wishlist(user=request.user, name=name, product_list=product_list)
        user_wishlist.save()
    
    elif user_wishlist != None:
        if wishlist == []:
            request.session['wishlist'] = make_wishlist_list(request, user_wishlist.product_list)
        
        elif wishlist != [] and user_wishlist.product_list != "":
            print('wishlist before merge', wishlist)            
            tmp_wishlist_db=make_wishlist_list(request, user_wishlist.product_list)
            print('tmp_wishlist_db', tmp_wishlist_db)            

            merged_wishlist = merge_wishlists(request, tmp_wishlist_db, wishlist)
            print('merged_wishlist', merged_wishlist)            

            user_wishlist.product_list = make_wishlist_string(request, merged_wishlist)
            user_wishlist.save()
            request.session['wishlist'] = merged_wishlist
        elif wishlist != [] and user_wishlist.product_list == "":
            user_wishlist.product_list = make_wishlist_string(request, wishlist)
            user_wishlist.save()
        return

