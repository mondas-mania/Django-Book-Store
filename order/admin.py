from django.contrib import admin
from .models import Order, OrderItem

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'card_number', 'cardholder_name', 'expiry_date', 'CVV_code', 'created', 'updated', 'paid']
    list_filter = ['paid', 'updated', 'created', 'user']
admin.site.register(Order, OrderAdmin)

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'book', 'price', 'quantity']
admin.site.register(OrderItem, OrderItemAdmin)
