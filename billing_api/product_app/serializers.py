from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from product_app.models import Product

class ProductSerializer(ModelSerializer):

    # Champ qui ne sera pas inclus lors d'une requête PUT ou POST
    category = serializers.CharField(read_only=True)

    class Meta:
        model = Product
        #fields = ['id', 'designation', 'description', 'price']
        fields = ['id', 'designation', 'category', 'description', 'price']
        # fields = '__all__'


