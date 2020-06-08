from django.test import TestCase

class TestAccountsViews(TestCase):

    def test_index_page_response(self):
        page = self.client.get("/", content_type="html/text", follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "products.html")