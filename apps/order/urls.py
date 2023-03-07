from django.urls import path
from .views import CardItemAPI, OrderAPI, OrderListAPI, StripeCheckoutAPI, CampaignAPI, SliderAPI

urlpatterns = [
    path('item/', CardItemAPI.as_view()),
    path('create/', OrderAPI.as_view()),
    path('list/', OrderListAPI.as_view()),
    path('stripe/', StripeCheckoutAPI.as_view()),
    path('slider/', SliderAPI.as_view()),
    path('campaign/', CampaignAPI.as_view()),
]
