from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Product, Comment, Cart, CartItem, Contact


admin.site.register((Category,Comment, Cart, CartItem, Contact))

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title","price","image_tag"]
    # fields = ['image_tag']
    readonly_fields = ['image_tag']
    def image_tag(self, obj):
        return format_html('<img width="100" height="100" src="{}" />'.format(obj.image.url))

    image_tag.short_description = 'Image'

