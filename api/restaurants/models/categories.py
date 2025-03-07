from django.db import models

class Category(models.Model):
    idx = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    
    class Meta:
        db_table = 'categories'
        managed = False

    def __str__(self):
        return self.name

