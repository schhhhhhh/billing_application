from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from customer_app.models import Customer
from customer_app.serializers import CustomerSerializer

# Create your views here.

class ListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class DetailView(generics.RetrieveAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class UpdateView(generics.UpdateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class DeleteView(generics.DestroyAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
