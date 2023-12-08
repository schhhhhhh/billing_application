from django.shortcuts import render
from rest_framework import generics
from django.shortcuts import get_object_or_404

from product_app.models import Product
from category_app.models import Category

from product_app.serializers import ProductSerializer

from rest_framework.generics import CreateAPIView, UpdateAPIView

# Create your views here.


class ListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class DetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductCreateView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # Récupérer l'ID de la catégorie depuis l'URL
        category_id = self.kwargs.get('category_id')
        
        # Récupérer la catégorie correspondante
        # category = Category.objects.get(id=category_id)
        category = get_object_or_404(Category, id=category_id)

        # Enregistrer le produit avec la catégorie associée
        serializer.save(category=category)


class ProductUpdateView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_update(self, serializer):
        # Récupérer l'ID de la catégorie depuis l'URL
        category_id = self.kwargs.get('category_id')

        # Récupérer la catégorie correspondante
        #category = Category.objects.get(id=category_id)
        category = get_object_or_404(Category, id=category_id)

        # Mettre à jour le produit avec la nouvelle catégorie
        serializer.save(category=category)

class DeleteView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer