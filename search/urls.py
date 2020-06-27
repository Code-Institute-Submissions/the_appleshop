from django.conf.urls import url
from .views import do_search, do_search_reviews

urlpatterns = [
    url(r'^$', do_search, name='search'),
    url(r'^search_reviews/$', do_search_reviews, name='review_search'),
]