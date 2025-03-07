from django.db import models

class PriceRange(models.Model):
    idx = models.AutoField(primary_key=True)
    label = models.CharField(max_length=100, unique=True)
    
    class Meta:
        db_table = 'price_ranges'
        managed = False

    def __str__(self):
        return self.name
