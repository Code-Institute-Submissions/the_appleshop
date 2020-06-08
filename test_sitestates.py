from django.test import TestCase
from django.shortcuts import get_object_or_404

# Create your tests here.

class TestSitestates(TestCase):

    def test_get_active_app(self):
        page = self.client.get("/products/", content_type="html/text", follow_redirects=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "products.html")
        #get_active_app(request)
        #self.assertEqual({'app_path': app_path}, "/products/")
