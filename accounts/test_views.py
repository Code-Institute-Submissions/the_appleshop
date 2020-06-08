from django.test import TestCase
from django.shortcuts import get_object_or_404

# Create your tests here.

class TestAccountsViews(TestCase):

    def test_login_page_response(self):
        page = self.client.get("/accounts/login/", content_type="html/text", follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")
