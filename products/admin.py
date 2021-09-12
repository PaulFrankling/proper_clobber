""" Products admin.py """
from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    """ Admin display for product """
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    """ Admin display for category """
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
