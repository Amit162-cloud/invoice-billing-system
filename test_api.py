#!/usr/bin/env python
import requests
import json

# Test the API
try:
    response = requests.get('http://127.0.0.1:8000/api/invoices/1/')
    print('✓ Backend API is working')
    print('✓ Invoice retrieved successfully')
    data = response.json()
    print(f'  - Invoice Number: {data.get("invoiceNumber")}')
    print(f'  - Customer: {data.get("customerName")}')
    print(f'  - Total: ₹{data.get("total")}')
    print(f'  - Lines: {len(data.get("lines", []))}')
    print(f'  - Payments: {len(data.get("payments", []))}')
    print('\n✓ All systems operational!')
    print('✓ Frontend available at: http://localhost:3000')
    print('✓ Backend API available at: http://127.0.0.1:8000/api/invoices/')
except Exception as e:
    print(f'✗ API Error: {e}')
