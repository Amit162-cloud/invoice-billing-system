from django.urls import path
from . import views

urlpatterns = [
    path('', views.invoice_list, name='invoice-list'),
    path('<int:pk>/', views.get_invoice, name='invoice-detail'),
    path('<int:pk>/payments/', views.add_payment, name='add-payment'),
    path('archive/', views.archive_invoice, name='archive-invoice'),
    path('restore/', views.restore_invoice, name='restore-invoice'),
]

# Invoice lines endpoint
urlpatterns += [
    path('invoice-lines/', views.create_invoice_line, name='create-invoice-line'),
]
