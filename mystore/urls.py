from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
#from welcome.views import index, health
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
#    url(r'^cart/', include('cart.urls', namespace='cart')),
#    url(r'^orders/', include('orders.urls', namespace='orders')),
    url(r'^', include('books.urls', namespace='books')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
