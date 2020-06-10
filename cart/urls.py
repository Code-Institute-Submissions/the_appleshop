from django.conf.urls import url
from .views import view_cart, add_to_cart, adjust_cart
from .contexts import cart_contents
import os

if os.getenv("TESTING") == "True":

    urlpatterns = [
        url(r'^$', view_cart, name='view_cart'),
        url(r'^add/(?P<id>\d+)', add_to_cart, name='add_to_cart'),
        url(r'^adjust/(?P<id>\d+)', adjust_cart, name='adjust_cart'),
        url(r'^contents/$', cart_contents, name='cartcontents')
    ] 

else:
    urlpatterns = [
        url(r'^$', view_cart, name='view_cart'),
        url(r'^add/(?P<id>\d+)', add_to_cart, name='add_to_cart'),
        url(r'^adjust/(?P<id>\d+)', adjust_cart, name='adjust_cart'),
    ]