from django.contrib import admin
from .models import Book, Cart, Order, OrderItem, User,Category

admin.site.register(Book)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(User)
admin.site.register(Category)