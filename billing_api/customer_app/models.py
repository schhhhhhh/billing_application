from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.fields.CharField(max_length=100)
    first_name = models.fields.CharField(max_length=100)
    email_address = models.fields.CharField(max_length=100)
    address = models.fields.CharField(max_length=100)
    phone = models.fields.CharField(max_length=100)
    postal_code = models.fields.CharField(max_length=100)
    city = models.fields.CharField(max_length=100)
    country = models.fields.CharField(max_length=100)

    def __str__(self):
        return self.name