from django.urls import path

from product_app.views import DeleteView, DetailView, ListView, ProductCreateView, ProductUpdateView

urlpatterns = [
    path('product/', ListView.as_view(), name='list-View'),
    path('product/<int:pk>/', DetailView.as_view(), name='detail-View'),
    path('categories/<int:category_id>/products/create/', ProductCreateView.as_view(), name='product-create'),
    path('categories/<int:category_id>/products/<int:pk>/update/', ProductUpdateView.as_view(), name='product-update'),
    path('product/delete/<int:pk>/', DeleteView.as_view(), name='delete-View'),

]