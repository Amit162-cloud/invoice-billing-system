from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.viewsets import ModelViewSet

from .models import Invoice, InvoiceLine, Payment
from .serializers import InvoiceSerializer, InvoiceLineSerializer, PaymentSerializer
from .services import update_invoice_totals


# List and Create Invoices
@api_view(['GET', 'POST'])
def invoice_list(request):
    if request.method == 'GET':
        invoices = Invoice.objects.filter(isArchived=False).order_by('-id')
        serializer = InvoiceSerializer(invoices, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = InvoiceSerializer(data=request.data)
        if serializer.is_valid():
            invoice = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# GET Invoice Details
@api_view(['GET'])
def get_invoice(request, pk):
    try:
        invoice = Invoice.objects.get(pk=pk)
        serializer = InvoiceSerializer(invoice)
        return Response(serializer.data)
    except Invoice.DoesNotExist:
        return Response({"error": "Invoice not found"}, status=404)


# Add Payment
@api_view(['POST'])
def add_payment(request, pk):
    try:
        invoice = Invoice.objects.get(pk=pk)
    except Invoice.DoesNotExist:
        return Response({"error": "Invoice not found"}, status=404)

    amount = float(request.data.get("amount", 0))

    if amount <= 0:
        return Response({"error": "Amount must be > 0"}, status=400)

    if amount > invoice.balanceDue:
        return Response({"error": "Overpayment not allowed"}, status=400)

    payment = Payment.objects.create(
        invoice=invoice,
        amount=amount
    )

    update_invoice_totals(invoice)

    return Response(PaymentSerializer(payment).data)


# Archive
@api_view(['POST'])
def archive_invoice(request):
    pk = request.data.get("id")
    invoice = Invoice.objects.get(pk=pk)
    invoice.isArchived = True
    invoice.save()
    return Response({"message": "Archived"})


# Restore
@api_view(['POST'])
def restore_invoice(request):
    pk = request.data.get("id")
    invoice = Invoice.objects.get(pk=pk)
    invoice.isArchived = False
    invoice.save()
    return Response({"message": "Restored"})


# Create Invoice Line
@api_view(['POST'])
def create_invoice_line(request):
    serializer = InvoiceLineSerializer(data=request.data)
    if serializer.is_valid():
        line = serializer.save()
        # Update invoice totals
        update_invoice_totals(line.invoice)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
