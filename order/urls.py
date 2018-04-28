from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^create/$', views.order_create, name='order_create'),
    url(r'^pdf/(?P<order_id>[0-9]+)$', views.pdf, name='order_pdf'),
]
