from django.contrib import admin

from customer_app.models import Customer

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):  
    list_display = ('name', 'first_name', 'email_address') # liste les champs que nous voulons sur l'affichage de la liste

admin.site.register(Customer, CustomerAdmin) 