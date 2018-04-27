from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^detail/$', views.cart_detail, name='cart_detail'),
    url(r'^addbook/(?P<book_id>\d+)/$', views.cart_book_add, name='cart_book_add'),
    url(r'^removebook/(?P<book_id>\d+)/$', views.cart_book_remove, name='cart_book_remove'),
]
