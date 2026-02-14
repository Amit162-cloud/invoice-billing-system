from .models import Invoice


def update_invoice_totals(invoice):
    total = sum(line.lineTotal for line in invoice.lines.all())
    paid = sum(payment.amount for payment in invoice.payments.all())

    invoice.total = total
    invoice.amountPaid = paid
    invoice.balanceDue = total - paid

    if invoice.balanceDue <= 0:
        invoice.status = "PAID"

    invoice.save()
