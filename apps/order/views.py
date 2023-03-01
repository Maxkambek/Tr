from rest_framework import generics, permissions, response, views
from .serializers import OrderSerializer, CardItemSerializer, OrderListSerializer
from .models import Order, CardItem
import stripe
from django.conf import settings
from django.shortcuts import redirect

stripe.api_key = settings.STRIPE_SECRET_KEY


class StripeCheckoutAPI(views.APIView):
    def post(self, request):
        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        'price': 'price_1Mg47JCjSODrX02WDhTtgNku',
                        'quantity': 1,
                    }
                ],
                payment_method_types=['card', ],
                mode='payment',
                success_url='/',
                cancel_url='/',
            )
            return redirect(checkout_session.url)
        except:
            return response.Response({'msg': "Error"})


class OrderAPI(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def post(self, request, *args, **kwargs):
        data = self.request.data
        data['user'] = self.request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data)


class OrderListAPI(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).all()

    def get_serializer_class(self):
        return OrderListSerializer


class CardItemAPI(generics.CreateAPIView):
    queryset = CardItem.objects.all()
    serializer_class = CardItemSerializer
