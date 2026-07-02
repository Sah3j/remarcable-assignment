from django.contrib import admin
from .models import Category, Tag, Product

"""
Model registration for Product, Category and Tag
"""
admin.site.register(Category)
admin.site.register(Tag)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category")
    list_filter = ("category", "tags")
    search_fields = ("name", "description")
    filter_horizontal = ("tags",)
