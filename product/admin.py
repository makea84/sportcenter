from django.contrib import admin

from .models import Product, Stock, Line, Bill

admin.site.register(Product)
admin.site.register(Stock)
admin.site.register(Line)
admin.site.register(Bill)
