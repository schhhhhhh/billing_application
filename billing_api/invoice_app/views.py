import decimal
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views import View
import json

from invoice_app.serializers import InvoiceSerializer

from invoice_app.models import Invoice, InvoiceLine
from customer_app.models import Customer
from product_app.models import Product

# Create your views here.

class InvoiceView(View):

    permission_classes = [IsAuthenticated]
    
    def saveInvoiceLine(self, product_id, invoice_id, quantity):

        # Récupérer le produit correspondant
        product = get_object_or_404(Product, id = product_id)

        # Récupérer la facture correspondant
        invoice = get_object_or_404(Invoice, id = invoice_id)

        # Créer un nouvelle ligne de facture lié à la facture et au produit
        invoiceLine = InvoiceLine.objects.create(
            invoice = invoice,
            product = product,
            quantity = quantity,
            amount = product.price * quantity
        )

        # Retourner une réponse JSON indiquant que le invoiceLine a été créé avec succès
        # return JsonResponse({'message': 'Product created successfully', 'invoiceLine': invoiceLine})
        return invoiceLine
    
    def saveInvoice(self, customer_id):
        # Récupérer le customer correspondant
        customer = get_object_or_404(Customer, id = customer_id)

        # Créer un nouvelle facture lié au client
        invoice = Invoice.objects.create(
            customer = customer,
            amount_ht = 00.00,
            amount_tva = 00.00,
            amount_ttc = 00.00,
        )

        # Retourner une réponse JSON indiquant que le invoiceLine a été créé avec succès
        # return JsonResponse({'message': 'Product created successfully', 'invoice': invoice})
        return invoice
    
    def calculateInvoiceAmount(self, invoice_id):
        # Récupérer la facture correspondant
        invoice = get_object_or_404(Invoice, id = invoice_id)

        # print(f"\n {invoice['invoice_lines']}")

        amount_ht = 0
        amount_tva = 0

        for invoiceLine in invoice.invoice_lines.values():
            # amount_ht += invoiceLine['amount']
            amount_ht += decimal.Decimal(invoiceLine['amount'])

        print(f"\n {amount_ht}")

        amount_tva = amount_ht * decimal.Decimal(0.18)

        print(f"\n {amount_tva}")

        invoice.amount_ht = amount_ht
        invoice.amount_tva = amount_tva
        invoice.amount_ttc = amount_ht + amount_tva

        invoice.save()


    @csrf_exempt
    @swagger_auto_schema(
    method='post',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'products': openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'quantity': openapi.Schema(type=openapi.TYPE_INTEGER),
                        'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                    }
                )
            ),
            'customer_id': openapi.Schema(type=openapi.TYPE_INTEGER),
        },
        required=['products', 'customer_id'],
    ),
    responses={200: 'Example response description'}
    )
    @api_view(['POST'])
    def createInvoice(request, customer_id):

        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        # print(f"\n {request.body.decode('utf-8')}")
        # print(f"\n {request.body}")
        # print(f"\n {products}")

        # Récupérer le customer correspondant
        customer_id = body['customer_id']

        # Récupérer la liste des produits correspondants
        products = body['products']

        if request.method == 'POST':

            # Sauvegarder et récupérer la facture correspondante
            invoice = InvoiceView.saveInvoice(InvoiceView, customer_id)
            # Créer les ligne factures
            for product in products:
                InvoiceView.saveInvoiceLine(InvoiceView, product['id'], invoice.id, product['quantity'])

            # Calculer le montant de la facture
            InvoiceView.calculateInvoiceAmount(InvoiceView, invoice.id)

            invoice = get_object_or_404(Invoice, id = invoice.id)

            invoice_serializer = InvoiceSerializer(invoice, many=False)
            
            # return JsonResponse({'message': 'Invoice created successfully', 'invoice': invoice.id})
            # return JsonResponse({'message': 'Invoice created successfully', 'invoice': invoice_serializer.data})
            return JsonResponse(invoice_serializer.data, safe=False)
            
        # Si la méthode HTTP n'est ni POST ni PUT , renvoyer une erreur
        error_data = {'error': 'Invalid request method'}
        return JsonResponse(error_data, status=400)
    

    @csrf_exempt
    @swagger_auto_schema(
    method='put',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'products': openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'quantity': openapi.Schema(type=openapi.TYPE_INTEGER),
                        'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                    }
                )
            ),
            'invoice_id': openapi.Schema(type=openapi.TYPE_INTEGER),
        },
        required=['products', 'invoice_id'],
    ),
    responses={200: 'Facture mise à jour avec succes'}
    )
    @api_view(['PUT'])
    def updateInvoice(request, invoice_id):

        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        # Récupérer la liste des produits correspondants
        products = body['products']
        
        if request.method == 'PUT':

            # Récupérer l'id de la facture correspondante
            invoice_id = body['invoice_id']

            # Récupérer les ancienne lignes factures et les supprimées
            invoice = get_object_or_404(Invoice, id = invoice_id)
            invoice_lines = InvoiceLine.objects.filter(invoice_id = invoice_id)
            invoice_lines.delete()

            # Créer les ligne factures
            for product in products:
                InvoiceView.saveInvoiceLine(InvoiceView, product['id'], invoice_id, product['quantity'])

            # Calculer le montant de la facture
            InvoiceView.calculateInvoiceAmount(InvoiceView, invoice_id)

            invoice = get_object_or_404(Invoice, id = invoice_id)

            invoice_serializer = InvoiceSerializer(invoice, many=False)
            
            # return JsonResponse({'message': 'Invoice created successfully', 'invoice': invoice_id})
            # return JsonResponse({'message': 'Invoice created successfully', 'invoice': invoice_serializer.data})
            return JsonResponse(invoice_serializer.data, safe=False)
            
        # Si la méthode HTTP n'est ni POST ni PUT , renvoyer une erreur
        error_data = {'error': 'Invalid request method'}
        return JsonResponse(error_data, status=400)
    

    @csrf_exempt
    @api_view(['PUT'])
    def invoicePayment(request, invoice_id):
        if request.method == 'PUT':
            # Récupérer la facture correspondant
            invoice = get_object_or_404(Invoice, id = invoice_id)
            
            # Modifier le statut à true
            invoice.status = True
            invoice.save()

            invoice_serializer = InvoiceSerializer(invoice, many=False)

            return JsonResponse(invoice_serializer.data, safe=False)
        
        # Si la méthode HTTP n'est pas PUT, renvoyer une erreur
        error_data = {'error': 'Invalid request method'}
        return JsonResponse(error_data, status=400)
    

class ListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

class DetailView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

class DeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer