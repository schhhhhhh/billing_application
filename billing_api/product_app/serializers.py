from rest_framework.serializers import ModelSerializer

from product_app.models import Product

class ProductSerializer(ModelSerializer):
 
    class Meta:
        model = Product
        # fields = ['id', 'designation', 'category', 'description', 'price']
        fields = '__all__'


