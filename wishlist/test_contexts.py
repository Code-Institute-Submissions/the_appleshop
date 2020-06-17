from django.test import TestCase
from products.models import Product
from django.views.generic import View, TemplateView, RedirectView
from .contexts import make_wishlist_string, make_wishlist_list, merge_wishlists, get_and_update_wishlist, wishlist_contents
from django.contrib.auth.models import User
from .models import Wishlist


class TestWishlistContexts(TestCase):      

    def test_empty_wishlist_contents(self):
        wishlist = self.client.session.get('wishlist', [])
        self.assertEqual(wishlist, [])


    def test_wishlist_contents_return_values(self):
        product1 = Product.objects.create(name='Boskop', description='description testproduct', price=2)
        product2 = Product.objects.create(name='Golden delicious', description='description', price=1)      
        self.client.post('/wishlist/add/1')
        self.client.post('/wishlist/add/2')
        wishlist = self.client.session.get('wishlist', [])
        self.assertEqual(wishlist, [1, 2])
        response=self.client.get('/products/', content_type="html/text", follow=True)
        self.assertIn(b'Boskop', response.content)
        self.assertIn(b'Golden delicious', response.content)


class TestWishlistMethods(TestCase):
    def test_make_wishlist_string(self):
        wishlist = [1,2]
        self.assertEqual(make_wishlist_string(wishlist), '1,2')

    def test_make_wishlist_list_with_empty_product_list(self):
        productlist =""
        self.assertEqual(make_wishlist_list(productlist), [])
        
    def test_make_wishlist_list_with_with_product_list(self):
        productlist = '1,2'
        self.assertEqual(make_wishlist_list(productlist), [1,2])

    def test_merge_wishlists_both_lists_different_values(self):
        tmp_wishlist_from_db = [1]
        wishlist = [2]
        self.assertEqual(merge_wishlists(tmp_wishlist_from_db, wishlist), [2,1])

    def test_merge_wishlists_one_list_contains_other_list_value(self):
        tmp_wishlist_from_db = [1,2]
        wishlist = [2]
        self.assertEqual(merge_wishlists(tmp_wishlist_from_db, wishlist), [2,1])

    def test_merge_wishlists_tmp_list_empty(self):
        tmp_wishlist_from_db = []
        wishlist = [2]
        self.assertEqual(merge_wishlists(tmp_wishlist_from_db, wishlist), [2])

    def test_merge_wishlists_wishlist_empty(self):
        tmp_wishlist_from_db = [1,2]
        wishlist = []
        self.assertEqual(merge_wishlists(tmp_wishlist_from_db, wishlist), [1,2])
    

    def test_get_and_update_wishlist_with_wishlist_in_db(self):
        new_user = User.objects.create_user('testuser', 'testuser@domain.com', 'password')
        self.client.login(username='testuser', password='password')
        name = str(new_user)+"'s wishlist" 
        user_wishlist = Wishlist(user=new_user, name=name, product_list="1,2") 
        user_wishlist.save()
        response=self.client.get('/products/', content_type="html/text", follow=True)
        wishlist = self.client.session.get('wishlist', [])
        self.assertEqual(wishlist, [1,2])


    def test_get_and_update_wishlist_with_wishlist_in_db_no_locallist(self):
        new_user = User.objects.create_user('testuser', 'testuser@domain.com', 'password')
        self.client.login(username='testuser', password='password')
        name = str(new_user)+"'s wishlist" 
        user_wishlist = Wishlist(user=new_user, name=name, product_list="2,3") 
        user_wishlist.save()
        product1 = Product.objects.create(name='Boskop', description='description testproduct', price=2)
        product2 = Product.objects.create(name='Golden delicious', description='description', price=1)      
        product1.save()
        product2.save()
        response=self.client.get('/products/', content_type="html/text", follow=True)
        wishlist = self.client.session.get('wishlist', [])
        self.assertEqual(wishlist, [2,3])


    def test_get_and_update_wishlist_with_empty_wishlist_in_db_and_locallist(self):
        new_user = User.objects.create_user('testuser', 'testuser@domain.com', 'password')
        self.client.login(username='testuser', password='password')
        name = str(new_user)+"'s wishlist" 
        user_wishlist = Wishlist(user=new_user, name=name, product_list="") 
        user_wishlist.save()
        product1 = Product.objects.create(name='Boskop', description='description testproduct', price=2)
        product2 = Product.objects.create(name='Golden delicious', description='description', price=1)      
        self.client.post('/wishlist/add/1')
        self.client.post('/wishlist/add/2')
        response=self.client.get('/products/', content_type="html/text", follow=True)
        test_wishlist = Wishlist.objects.get(user=new_user)
        self.assertEqual(test_wishlist.product_list, '1,2')
