from django.urls import path

from category_app.views import CreateView, DetailView, DeleteView, ListView, UpdateView

urlpatterns = [
    path('category/', ListView.as_view(), name='list-View'),
    path('category/<int:pk>/', DetailView.as_view(), name='detail-View'),
    path('category/create/', CreateView.as_view(), name='create-View'),
    path('category/update/<int:pk>/', UpdateView.as_view(), name='update-View'),
    path('category/delete/<int:pk>/', DeleteView.as_view(), name='delete-View'),
]