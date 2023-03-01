from django.db import models
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='categories')

    def __str__(self):
        return self.name

    @property
    def get_icon(self):
        return f"{settings.SITE_URL}{self.icon.url}"


class Subcategory(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, models.CASCADE, related_name='subcategory')

    def __str__(self):
        return self.name


class Color(models.Model):
    COLORS = (
        ('FF0000', 'Red'),
        ('00FFFF', 'Cyan'),
        ('0000FF', 'Blue'),
        ('800080', 'Purple'),
        ('FFFF00', 'Yellow'),
        ('FFFFFF', 'White'),
        ('000000', 'Black'),
        ('008000', 'Green'),
        ('C0C0C0', 'Silver'),
        ('FF00FF', 'Magenta'),
        ('FFA500', 'Orange'),
        ('800000', 'Maroon'),
        ('808000', 'Olive'),
    )
    name = models.CharField(max_length=6, choices=COLORS)

    def __str__(self):
        return self.get_name_display()


class Brand(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    new_price = models.PositiveIntegerField(null=True, blank=True)
    is_delivery = models.BooleanField(default=False)
    price_delivery = models.PositiveIntegerField(null=True, blank=True)
    phone = models.BooleanField(default=False)
    type_cash = models.CharField(max_length=255)
    return_day = models.PositiveIntegerField()
    category = models.ForeignKey(Subcategory, models.SET_NULL, null=True)
    brand = models.ForeignKey(Brand, models.SET('No brand'), related_name='product')
    made_in = models.CharField(max_length=255)
    color = models.ManyToManyField(Color)
    description = models.TextField()
    characteristic = models.CharField(max_length=255)
    rating = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def get_rating(self):
        user_count = self.rate.all().count()
        if user_count == 0:
            user_count = 1
        rate_summa = sum([item.rate for item in self.rate.all()])
        self.rating = rate_summa / user_count
        self.save()
        return self.rating

    class Meta:
        ordering = ['rating']


class ProductImage(models.Model):
    product = models.ForeignKey(Product, models.CASCADE, related_name='product_image')
    image = models.ImageField(upload_to='product_images')

    @property
    def get_image_url(self):
        return f"{settings.SITE_URL}{self.image.url}"
