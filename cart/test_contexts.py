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
        product1.save()
        product2.save()
        self.client.post('/cart/add/1', data={'quantity': 11})
        self.client.post('/cart/add/2', data={'quantity': 22})
        cart = self.client.session.get('cart', {})
        self.assertEqual(cart, {'1': 11, '2': 22})

        


