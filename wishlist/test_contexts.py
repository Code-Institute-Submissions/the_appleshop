from django.test import TestCase
from .views import view_wishlist, add_to_wishlist, remove_from_wishlist
from products.models import Product
from django.views.generic import View, TemplateView, RedirectView


class TestWishlistContext(TestCase):

    def test_response_wishlist_view(self):
        response = self.client.get("/wishlist/", content_type="html/text", follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "wishlist.html")        

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

        