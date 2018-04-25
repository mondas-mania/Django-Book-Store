from django.conf.urls import url
from . import views


urlpatterns = [
	#url(r'^$', views.go_books, name='book_list'),
	url(r'^$', views.product_list, name='product_list'),
]