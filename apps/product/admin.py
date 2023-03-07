from django.contrib import admin
from .models import Category, Subcategory, Product, ProductImage, Color, Brand, ThreeSubcategory
from .translation import CustomTranslationsAdmin


@admin.register(Category)
class CategoryAdmin(CustomTranslationsAdmin):
    list_display = ['id', 'name']


@admin.register(ThreeSubcategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'subcategory']


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(Color)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(Subcategory)
class CategoryAdmin(CustomTranslationsAdmin):
    list_display = ['id', 'category']


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


@admin.register(Product)
class ProductAdmin(CustomTranslationsAdmin):
    inlines = [ProductImageInline]
    list_display = ['id', 'name', 'price']
    filter_horizontal = ['color']


@admin.register(ProductImage)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id']
