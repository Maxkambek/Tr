# Generated by Django 3.2.18 on 2023-03-01 12:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '0001_initial'),
        ('product', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='rate',
            name='user',
            field=models.ForeignKey(on_delete=models.SET('User deleted'), related_name='rate', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='order',
            name='card_items',
            field=models.ManyToManyField(to='order.CardItem'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=models.SET('User deleted'), related_name='order', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='carditem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='card_item', to='product.product'),
        ),
    ]
