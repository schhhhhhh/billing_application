from django.urls import path

from customer_app.views import CreateView, DetailView, DeleteView, ListView, UpdateView

urlpatterns = [
    path('customer/', ListView.as_view(), name='list-View'),
    path('customer/<int:pk>/', DetailView.as_view(), name='detail-View'),
    path('customer/create/', CreateView.as_view(), name='create-View'),
    path('customer/update/<int:pk>/', UpdateView.as_view(), name='update-View'),
    path('customer/delete/<int:pk>/', DeleteView.as_view(), name='delete-View'),
]