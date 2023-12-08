from django.db import models

# Create your models here.


class Category(models.Model):
    designation = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.designation
