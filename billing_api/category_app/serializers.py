from rest_framework.serializers import ModelSerializer

from category_app.models import Category

from product_app.serializers import ProductSerializer

class CategorySerializer(ModelSerializer):

    # On spécifie avec read_only=True que le champs products
    # ne sera pas prise en compte pour un Create ou un update
    products = ProductSerializer(many=True, read_only=True)
 
    class Meta:
        model = Category
        fields = ['id', 'designation', 'description', 'products']
