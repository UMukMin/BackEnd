from django.db import models
from rest_framework.fields import IntegerField

class Region(models.Model):
    idx = models.IntegerField()

    class Meta:
        db_table = 'regions'
        managed = False

class Category(models.Model):
    idx = models.IntegerField()

    class Meta:
        db_table = 'categories'
        managed = False

class Restaurants(models.Model):
    idx = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null= True)
    region_idx = models.ForeignKey(Region, on_delete=models.CASCADE, db_column='region_idx', null=True)
    category_idx = models.ForeignKey(Category, on_delete=models.CASCADE, db_column='category_idx', null=True)
    address = models.CharField(max_length=255)
    opening_hours = models.CharField(max_length=100)
    description = models.TextField()
    average_rating = models.DecimalField(max_digits=3, decimal_places=2)
    number_of_ratings = models.IntegerField()
    price_range = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    payment_methods = models.CharField(max_length=100)
    reservation_available = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'restaurants'
        managed = False

    def __str__(self):
        return self.name