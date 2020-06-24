from django.conf.urls import url
from .views import get_reviews, review_detail, create_or_edit_review, delete_review, create_review

urlpatterns = [
    url(r'^$', get_reviews, name='get_reviews'),
    url(r'^(?P<id>\d+)/$', get_reviews, name='get_reviews'),
    url(r'^(?P<id>\d+)$', review_detail, name='review_detail'),
    url(r'^new/$', create_review, name='new_review'),
    url(r'^edit/(?P<id>\d+)/$', create_or_edit_review, name='edit_review'),
    url(r'^delete/(?P<id>\d+)/$', delete_review, name='delete_review'),
]
