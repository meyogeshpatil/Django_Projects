from django.db import models

# Create your models here.
class item(models.Model):
    product=models.CharField(max_length=100)
    desc=models.CharField(max_length=100)
    price=models.FloatField()
    def __str__(self):
        return self.product
