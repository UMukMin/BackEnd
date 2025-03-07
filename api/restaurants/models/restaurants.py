from django.db import models
from .categories import Category
from .price_ranges import PriceRange

class Restaurants(models.Model):
    idx = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, to_field='idx', db_column='category_idx')
    region = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    number_of_ratings = models.IntegerField(default=0)
    price_range = models.ForeignKey(PriceRange, on_delete=models.SET_NULL, db_column='price_range_idx', null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    reservation_available = models.BooleanField(default=False)
    opening_hours = models.TextField(null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'restaurants'
        managed = False

    def __str__(self):
        return self.name
