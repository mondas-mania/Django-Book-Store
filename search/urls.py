from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^results/$', views.search_book, name='search_book'),
]
