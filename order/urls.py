from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^create/$', views.order_create, name='order_create'),
    url(r'^shipping/(?P<order_id>[0-9]+)$', views.shipping_pdf, name='shipping_pdf'),
    url(r'^invoice/(?P<order_id>[0-9]+)$', views.invoice_pdf, name='invoice_pdf'),
]
