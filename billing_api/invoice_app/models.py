from django.db import models

from django.core.validators import MinValueValidator

from product_app.models import Product

from customer_app.models import Customer

# Create your models here.

class Invoice(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE, related_name='customer')
    status = models.BooleanField(default=False)
    amount_ht = models.DecimalField(max_digits=4, decimal_places=2)
    amount_tva = models.DecimalField(max_digits=4, decimal_places=2)
    amount_ttc = models.DecimalField(max_digits=4, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.amount_ttc
    

class InvoiceLine(models.Model):
    invoice = models.ForeignKey(Invoice, null=True, on_delete=models.CASCADE)
    produit = models.ForeignKey(Product, null=True, on_delete=models.CASCADE, related_name='invoice_lines')
    quantity = models.fields.IntegerField(
    validators=[MinValueValidator(1)]
    )
    amount = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.amount