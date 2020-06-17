from django.test import TestCase
from django.contrib.auth.models import User
from .backends import EmailAuth

# class TestEmailAuthClass(TestCase):
#     def test_user_authentication_with_correct_credentials(self):
#         new_user = User.objects.create_user('testuser', 'testuser@domain.com', 'password')
#         new_email_auth = EmailAuth()
#         new_email_auth.authenticate(username='testuser@domain.com', password='password')
#         self.assertEqual(new_email_auth.authenticate, new_user)
