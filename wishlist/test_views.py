from django.test import TestCase
from django.contrib.auth.models import User
#from .views import view_wishlist, add_to_wishlist, remove_from_wishlist



class TestWishlistViews(TestCase):
    def test_response_wishlist_view(self):
        response = self.client.get("/wishlist/", content_type="html/text", follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "wishlist.html")  

    def test_add_to_wishlist(self):
        response = self.client.get("/wishlist/", content_type="html/text", follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "wishlist.html")  