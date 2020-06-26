from django.test import TestCase
from .models import Review
from django.contrib.auth.models import User
from products.models import Product


class TestReviewViews(TestCase):

    def test_get_reviews_view(self):
        new_user = User.objects.create_user('testuser', 'testuser@domain.com', 'password')
        product1 = Product.objects.create(name='testproduct1', description='description testproduct1', price=1)
        product1.save()
        new_review = Review(title="review name", product=product1, author=new_user, rating=5, comment="Fantastic!")
        new_review.save()
        response=self.client.get('/reviews/', content_type="html/text", follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "reviews.html")
        self.assertIn(b'Fantastic!', response.content)


    def test_review_detail_view(self):
        new_user = User.objects.create_user('testuser', 'testuser@domain.com', 'password')
        product1 = Product.objects.create(name='testproduct1', description='description testproduct1', price=1)
        product1.save()
        new_review = Review(title="review name", product=product1, author=new_user, rating=5, comment="Fantastic!")
        new_review.save()
        response=self.client.get('/reviews/1', content_type="html/text", follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "reviewdetail.html")
        self.assertIn(b'Fantastic!', response.content)
        check_review = Review.objects.get(pk=1)
        self.assertEqual(check_review.view_count, 1)


    def test_create_review_view(self):
        new_user = User.objects.create_user('testuser', 'testuser@domain.com', 'password')
        self.client.login(username='testuser', password='password')
        product1 = Product.objects.create(name='testproduct1', description='description testproduct1', price=1)
        product1.save()
        response=self.client.get('/reviews/new/1', content_type="html/text", follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "editform.html")
        self.assertIn(b'required-field', response.content)


    def test_create_review_with_post_view(self):
        new_user = User.objects.create_user('testuser', 'testuser@domain.com', 'password')
        self.client.login(username='testuser', password='password')
        product1 = Product.objects.create(name='testproduct1', description='description testproduct1', price=1)
        product1.save()
        #new_review = Review(title="review name", author=new_user, rating=5, comment="Fantastic!")
        response=self.client.post('/reviews/new/', data={'title': 'review name', 'author': new_user, 'rating': 5, 'comment': 'Fantastic!'})
        self.assertTemplateUsed(response, "reviewdetail.html")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'required-field', response.content)






