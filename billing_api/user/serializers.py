from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

from product_app.models import Product

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


