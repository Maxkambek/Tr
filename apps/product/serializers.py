from rest_framework import serializers
from .models import Product, Category, Subcategory, ProductImage, Color, Brand


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


class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ['name']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'get_icon']



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
