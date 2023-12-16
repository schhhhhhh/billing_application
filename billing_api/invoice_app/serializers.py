from rest_framework.serializers import ModelSerializer

from invoice_app.models import Invoice, InvoiceLine

class InvoiceLineSerializer(ModelSerializer):

    class Meta:
        model = InvoiceLine
        fields = ['id', 'quantity', 'amount', 'product', 'getProduct']

class InvoiceSerializer(ModelSerializer):

    invoice_lines = InvoiceLineSerializer(many=True, read_only=True)

    class Meta:
        model = Invoice
        fields = ['id', 'getCustomer', 'amount_ttc', 'amount_tva', 'amount_ht', 'invoice_lines', 'status', 'created_at']