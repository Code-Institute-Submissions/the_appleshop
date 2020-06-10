from django.test import TestCase
from .views import add_to_cart
from products.models import Product
from django.views.generic import View, TemplateView, RedirectView


class TestCartContents(TestCase):

    def test_empty_cart_contents(self):
        cart = self.client.session.get('cart', {})
        self.assertEqual(cart, {})


    def test_cart_contents_return_values(self):
        product1 = Product.objects.create(name='Boskop', description='description testproduct', price=2)
        product2 = Product.objects.create(name='Golden delicious', description='description', price=1)      
        self.client.post('/cart/add/1', data={'quantity': 11})
        self.client.post('/cart/add/2', data={'quantity': 22})
        
        """
        response=self.client.get('/cart/contents/')
        print(testobject)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(cart_items, {'id': '1', 'quantity': 11, 'product': product1}, {'id': '2', 'quantity': 22, 'product': product2})
        self.assertEqual(total, 44)
        self.assertEqual(product_count, 33)
        """


