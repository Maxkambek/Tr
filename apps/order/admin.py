from django.contrib import admin
from .models import Order, Slider, Campaign


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'status', 'get_total', 'get_count', 'created_at']
    list_filter = ['status']
    filter_horizontal = ['card_items']


@admin.register(Slider)
class Admin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(Campaign)
class Admin(admin.ModelAdmin):
    list_display = ['id']
