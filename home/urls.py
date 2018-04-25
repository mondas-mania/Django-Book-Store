from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.product_list, name='product_list'),
	url(r'^terms/$', views.terms_and_conditions, name='ts_and_cs'),
	url(r'^contact/$', views.contact_us, name='contact'),
]