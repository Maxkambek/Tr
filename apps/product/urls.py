from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListAPI.as_view()),
    path('<int:pk>/', views.ProductDetailAPI.as_view()),
    path('category/', views.CategoryListAPI.as_view()),
    path('category/<int:pk>/', views.CategoryDetailAPI.as_view()),
    path('subcategory/', views.SubcategoryAPI.as_view()),
    path('threesubcategory/', views.ThreeSubcategoryAPI.as_view()),
    path('filter/', views.ProductFilterAPI.as_view()),
    path('colors/', views.ColorListAPI.as_view()),
    path('brands/', views.BrandListAPI.as_view()),
]
