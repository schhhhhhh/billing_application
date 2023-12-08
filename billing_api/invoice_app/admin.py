from django.contrib import admin

from invoice_app.models import Invoice, InvoiceLine

# Register your models here.
class InvoiceAdmin(admin.ModelAdmin):  
    list_display = ('customer', 'status', 'amount_ht', 'amount_ttc') # liste les champs que nous voulons sur l'affichage de la liste

admin.site.register(Invoice, InvoiceAdmin) 

class InvoiceLineAdmin(admin.ModelAdmin):  
    list_display = ('invoice', 'produit', 'quantity') # liste les champs que nous voulons sur l'affichage de la liste

admin.site.register(InvoiceLine, InvoiceLineAdmin) 