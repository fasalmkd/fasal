from django.db import models

class Product(models.Model):
    item=models.CharField(max_length=30)
    price=models.IntegerField()
    image=models.TextField(max_length=300)
    def __str__(self):
        return self.item

# Create your models here.
