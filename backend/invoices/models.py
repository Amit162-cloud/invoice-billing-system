from django.db import models

# Create your models here.
class Invoice(models.Model):
    STATUS_CHOICES = [
        ('DRAFT', 'Draft'),
        ('PAID', 'Paid'),
    ]

    invoiceNumber = models.CharField(max_length=50)
    customerName = models.CharField(max_length=100)
    issueDate = models.DateField()
    dueDate = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='DRAFT')

    total = models.FloatField(default=0)
    amountPaid = models.FloatField(default=0)
    balanceDue = models.FloatField(default=0)

    isArchived = models.BooleanField(default=False)

    def __str__(self):
        return self.invoiceNumber


class InvoiceLine(models.Model):
    invoice = models.ForeignKey(Invoice, related_name="lines", on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    quantity = models.IntegerField()
    unitPrice = models.FloatField()
    lineTotal = models.FloatField()

    def save(self, *args, **kwargs):
        self.lineTotal = self.quantity * self.unitPrice
        super().save(*args, **kwargs)


class Payment(models.Model):
    invoice = models.ForeignKey(Invoice, related_name="payments", on_delete=models.CASCADE)
    amount = models.FloatField()
    paymentDate = models.DateField(auto_now_add=True)