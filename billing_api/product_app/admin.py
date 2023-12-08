from django.contrib import admin

from product_app.models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):  
    list_display = ('designation', 'description', 'price', 'category') # liste les champs que nous voulons sur l'affichage de la liste

admin.site.register(Product, ProductAdmin) 