from django.db import models

from category_app.models import Category

# Create your models here.

class Product(models.Model):
    designation = models.fields.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.designation