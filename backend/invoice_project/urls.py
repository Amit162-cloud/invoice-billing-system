from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def api_root(request):
    return JsonResponse({
        "message": "Invoice API",
        "endpoints": {
            "invoices": "/api/invoices/",
            "admin": "/admin/"
        }
    })

urlpatterns = [
    path('', api_root),
    path('admin/', admin.site.urls),
    path('api/invoices/', include('invoices.urls')),
]
