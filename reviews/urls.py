from django.conf.urls import url
from .views import get_reviews, review_detail, create_or_edit_review, delete_review

urlpatterns = [
    url(r'^$', get_reviews, name='get_reviews'),
    url(r'^(?P<id>\d+)/$', review_detail, name='review_detail'),
    url(r'^(?P<id>\d+)/edit/$', create_or_edit_review, name='edit_review'),
    url(r'^(?P<id>\d+)/delete$', delete_review, name='delete_review'),
]
