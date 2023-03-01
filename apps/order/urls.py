from django.urls import path
from .views import CardItemAPI, OrderAPI, OrderListAPI, StripeCheckoutAPI

urlpatterns = [
    path('item/', CardItemAPI.as_view()),
    path('create/', OrderAPI.as_view()),
    path('list/', OrderListAPI.as_view()),
    path('stripe/', StripeCheckoutAPI.as_view()),
]
