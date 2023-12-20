from django.urls import path

from product_app.views import DeleteView, DetailView, ListView, ProductCreateView, ProductUpdateView

urlpatterns = [
    path('product/', ListView.as_view(), name='list-View'),
    path('product/<int:pk>/', DetailView.as_view(), name='detail-View'),
    path('product/category/<int:category_id>/create/', ProductCreateView.as_view(), name='product-create'),
    path('product/<int:pk>/category/<int:category_id>/update/', ProductUpdateView.as_view(), name='product-update'),
    path('product/delete/<int:pk>/', DeleteView.as_view(), name='delete-View'),

]