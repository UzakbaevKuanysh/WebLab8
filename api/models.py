from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length = 100)
    price = models.FloatField(max_length = 50)
    description = models.TextField(max_length=50)
    count = models.IntegerField()
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, blank = True, on_delete=models.CASCADE, default = 1)
    def __str__(self):
        return self.name


