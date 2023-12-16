from django.db import models

from django.core.validators import MinValueValidator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from product_app.serializers import ProductSerializer
from customer_app.serializers import CustomerSerializer

from product_app.models import Product

from customer_app.models import Customer

# Create your models here.

class Invoice(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE, related_name='customer')
    status = models.BooleanField(default=False)
    amount_ht = models.DecimalField(max_digits=20, decimal_places=2)
    amount_tva = models.DecimalField(max_digits=20, decimal_places=2)
    amount_ttc = models.DecimalField(max_digits=20, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.amount_ttc) + ' ' + self.customer.name
    
    def getCustomer(self):
        customer_serializer = CustomerSerializer(self.customer)
        return customer_serializer.data

class InvoiceLine(models.Model):
    invoice = models.ForeignKey(Invoice, null=True, on_delete=models.CASCADE, related_name='invoice_lines')
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE, related_name='invoice_lines')
    quantity = models.fields.IntegerField(
    validators=[MinValueValidator(1)]
    )
    amount = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return str(self.amount)

    def getProduct(self):
        product_serializer = ProductSerializer(self.product)
        return product_serializer.data