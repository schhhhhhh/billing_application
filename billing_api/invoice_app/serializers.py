from rest_framework.serializers import ModelSerializer

from invoice_app.models import Invoice

class InvoiceSerializer(ModelSerializer):
 
    class Meta:
        model = Invoice
        fields = ['id', 'name', 'category']