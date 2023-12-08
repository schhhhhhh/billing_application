from rest_framework.serializers import ModelSerializer

from customer_app.models import Customer


class CustomerSerializer(ModelSerializer):
 
    class Meta:
        model = Customer
        fields = '__all__'


