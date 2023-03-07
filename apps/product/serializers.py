from rest_framework import serializers
from .models import Product, Category, Subcategory, ProductImage, Color, Brand, ThreeSubcategory


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['get_name_display', 'name']


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['name']


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['get_image_url']


class ThreeSubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ThreeSubcategory
        fields = ['id', 'name']


class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ['id', 'name', 'three_subcategory']

    three_subcategory = ThreeSubcategorySerializer(many=True, read_only=True)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'get_icon', 'subcategory']

    subcategory = SubcategorySerializer(many=True, read_only=True)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'get_rating', 'product_image', 'description']

    product_image = ProductImageSerializer(many=True, read_only=True)


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'price', 'is_delivery', 'price_delivery', 'new_price', 'made_in', 'brand', 'color',
                  'return_day', 'type_cash', 'description', 'category', 'product_image']

    product_image = ProductImageSerializer(many=True)
