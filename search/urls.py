from django.conf.urls import url
from .views import do_search, do_ext_search

urlpatterns = [
    url(r'^$', do_search, name='search'),
    url(r'^ext_search/$', do_ext_search, name='ext_search'),

]