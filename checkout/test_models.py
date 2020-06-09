from django.test import TestCase
from django.db import models
from products.models import Product
from .models import Order, OrderLineItem

class TestCheckoutModels(TestCase):

    def test_Order_Model(self):
        order = Order.objects.create(full_name='John Doe',
                                     phone_number='123456789',
                                     country='Netherlands',
                                     postcode='1234',
                                     town_or_city='Amsterdam',
                                     street_address1='Street',
                                     street_address2='22',
                                     county='North',
                                     date='2020-06-09')
        
        order.save()
        #self.assertEqual(order, '1-2020-06-09-John Doe')
        self.assertEqual(order.id, 1)
        self.assertEqual(order.date, '2020-06-09')
        self.assertEqual(order.full_name, 'John Doe')

"""
    def test_order_line_item_Model(self):
        order = Order.objects.create(full_name='John Doe',
                                     phone_number='123456789',
                                     country='Netherlands',
                                     postcode='1234',
                                     town_or_city='Amsterdam',
                                     street_address1='Street',
                                     street_address2='22',
                                     county='North',
                                     date='2020-06-09')
        #order.save()
        product = Product.objects.create(name='testproduct', description='description testproduct', price=2)
        product.save()
        order_line_item= OrderLineItem(order=order,
                                       product=product,
                                       quantity=2)
        self.assertEqual(order_line_item.quantity, 2)
        self.assertEqual(order_line_item.product.name, 'testproduct')
        self.assertEqual(order_line_item.product.price, 2)
"""