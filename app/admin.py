from django.contrib import admin
from .models import Customer, Product, Customization, Order, OrderItem


admin.site.register(Customer)

admin.site.register(Product)

admin.site.register(Customization)

admin.site.register(Order)

admin.site.register(OrderItem)

