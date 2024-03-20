from rest_framework.serializers import ModelSerializer

from user.serializers import UserSerializer

from invoice_app.models import Invoice, InvoiceLine

class InvoiceLineSerializer(ModelSerializer):

    class Meta:
        model = InvoiceLine
        fields = ['id', 'quantity', 'amount', 'product', 'getProduct']

class InvoiceSerializer(ModelSerializer):

    created_by = UserSerializer()  # UserSerializer pour le champ created_by
    updated_by = UserSerializer()  # UserSerializer pour le champ updated_by
    validate_by = UserSerializer()  # UserSerializer pour le champ validate_by

    invoice_lines = InvoiceLineSerializer(many=True, read_only=True)

    class Meta:
        model = Invoice
        fields = ['id', 'getCustomer', 'amount_ttc', 'amount_tva', 'amount_ht', 'invoice_lines', 'status', 'created_at', 'updated_at', 'created_by', 'updated_by', 'validate_by']