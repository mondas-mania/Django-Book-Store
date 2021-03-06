from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views as core_views


urlpatterns = [
    # specify URL patterns for login, logout and new user registration ('signup')
    url(r'^login/$', auth_views.login, {'template_name': 'account/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'account/logged_out.html'}, name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^orders/$', core_views.orderHistory, name='orders'),
]
