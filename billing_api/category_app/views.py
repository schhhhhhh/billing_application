from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


from category_app.models import Category
from category_app.serializers import CategorySerializer

# Create your views here.

class ListView(generics.ListAPIView):
    # Nous avons simplement à appliquer la permission sur le ListAPIViews
    # permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class DetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class UpdateView(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class DeleteView(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
