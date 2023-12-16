# urls.py
from django.urls import path

from invoice_app.views import DeleteView, DetailView, InvoiceView, ListView

urlpatterns = [
    path('invoice/', ListView.as_view(), name='list-View'),
    path('invoice/<int:pk>/', DetailView.as_view(), name='detail-View'),
    path('invoice/customer/<int:customer_id>/create', InvoiceView.createInvoice, name='view-create'),
    path('invoice/<int:invoice_id>/payment', InvoiceView.invoicePayment, name='invoice-payment'),
    path('invoice/delete/<int:pk>/', DeleteView.as_view(), name='delete-View'),


]
