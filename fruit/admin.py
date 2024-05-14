from django.contrib import admin

from .models import Category, Product, Comment, Cart, CartItem, Contact


admin.site.register((Category, Product, Comment, Cart, CartItem, Contact))
