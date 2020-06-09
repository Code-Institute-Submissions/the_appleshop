from django.test import TestCase
from products.models import Product

class TestSearchView(TestCase):
    def test_do_search(self):
        product = Product.objects.create(name='testproduct', description='description testproduct', price=2)
        page=self.client.get("/search/", data={'q': product}, follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "products.html")
        self.assertIn(b'testproduct', page.content)


