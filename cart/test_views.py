from django.test import TestCase
from products.models import Product


class TestAddToCartViews(TestCase):

    def test_response_view_cart(self):
        response = self.client.get("/cart/", content_type="html/text", follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "cart.html")


    def test_add_products_not_being_on_cart(self):
        self.client.post('/cart/add/1', data={'quantity': 11})
        self.client.post('/cart/add/2', data={'quantity': 22})
        cart = self.client.session.get('cart')
        self.assertEqual(cart, {'1': 11, '2': 22})


    def test_add_product_already_being_on_cart(self):
        self.client.post('/cart/add/1', data={'quantity': 11})
        self.client.post('/cart/add/1', data={'quantity': 11})
        cart = self.client.session.get('cart')
        self.assertEqual(cart, {'1': 22})


class TestAdjustCartViews(TestCase):

    def test_increase_product_quantity_on_cart(self):
        self.client.post('/cart/add/1', data={'quantity': 11})
        self.client.post('/cart/adjust/1', data={'quantity': 5})
        cart = self.client.session.get('cart')
        self.assertEqual(cart, {'1': 5})


    def test_set_product_quantity_on_cart_to_zero(self):
        self.client.post('/cart/add/1', data={'quantity': 11})
        self.client.post('/cart/adjust/1', data={'quantity': 0})
        cart = self.client.session.get('cart')
        self.assertEqual(cart, {})
