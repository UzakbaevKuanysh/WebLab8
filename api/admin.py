from itertools import product
from django.contrib import admin

from api.models import Category, Product

# Register your models here.
admin.site.register(Product)

admin.site.register(Category)
