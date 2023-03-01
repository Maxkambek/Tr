from rest_framework import generics, views, response
from .models import Product, Category, Color, Brand
from .serializers import ProductSerializer, ProductDetailSerializer, CategorySerializer, ColorSerializer, \
    BrandSerializer
from django.db.models import Q


class CategoryListAPI(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BrandListAPI(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class ColorListAPI(generics.ListAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class ProductListAPI(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        qs = self.queryset.all()
        cat = self.request.query_params.get('cat')
        subcategory = self.request.query_params.get('subcat')
        brand = self.request.query_params.get('brand')
        color = self.request.query_params.get('color')
        if cat:
            qs = self.queryset.filter(category__category__name__exact=cat)
        if subcategory:
            qs = self.queryset.filter(Q(category__category__name__exact=cat), Q(category__name__exact=subcategory))
        if brand:
            qs = self.queryset.filter(Q(category__category__name__exact=cat), Q(category__name__exact=subcategory),
                                      Q(brand=brand))
        if color:
            qs = self.queryset.filter(Q(category__category__name__exact=cat), Q(category__name__exact=subcategory),
                                      Q(brand=brand),
                                      Q(color=color))
        return qs


class ProductDetailAPI(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


class ProductFilterAPI(views.APIView):
    queryset = Product.objects.all()

    def get(self, request, *args, **kwargs):
        data = dict()
        made_ins = self.queryset.order_by('made_in').distinct('made_in').all()
        data['made_ins'] = f"{made_ins.first().made_in}({made_ins.count()})"
        print(data)
        return response.Response(data)
