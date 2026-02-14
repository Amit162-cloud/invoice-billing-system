<<<<<<< HEAD
# Invoice Management Application

A full-stack web application for managing invoices with a professional UI inspired by Monefy. Built with Django REST Framework backend and React frontend.

## Features

- 📄 **Create and manage invoices** with unlimited line items
- 💰 **Track payments** with automatic balance calculations
- 📊 **Dashboard** with invoice statistics and overview
- 🏗️ **Invoice details page** with payment history
- 📈 **Real-time total calculations** for invoice amounts
- 🔐 **Admin panel** for direct database management
- 📱 **Responsive design** for desktop and mobile

## Tech Stack

### Backend
- **Framework**: Django 6.0.2
- **API**: Django REST Framework
- **Database**: SQLite
- **Language**: Python 3

### Frontend
- **Framework**: React 19.2.4
- **Routing**: React Router v7
- **HTTP Client**: Axios
- **Styling**: CSS with design variables
- **Language**: JavaScript/JSX

## Prerequisites

Before running the application, ensure you have installed:

- **Python 3.8+** ([Download](https://www.python.org/downloads/))
- **Node.js 14+** and **npm** ([Download](https://nodejs.org/))
- **Git** (optional, for version control)

Verify installation:
```bash
python --version
node --version
npm --version
```

## Setup Instructions

### 1. Clone or Download the Project

```bash
# If using git
git clone <repository-url>
cd invoice-project

# If downloaded as zip, just extract and navigate to the folder
cd invoice-project
```

### 2. Backend Setup

#### Step 1: Navigate to backend directory
```bash
cd backend
```

#### Step 2: Create a Python virtual environment (recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

#### Step 3: Install Python dependencies
```bash
pip install -r ../requirement.txt
```

#### Step 4: Run database migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

#### Step 5: Create an admin user (optional)
```bash
python manage.py createsuperuser
```
Or use the default credentials:
- **Username**: `admin`
- **Password**: `admin123`

### 3. Frontend Setup

#### Step 1: Navigate to frontend directory (in a new terminal/PowerShell)
```bash
cd frontend
```

#### Step 2: Install Node dependencies
```bash
npm install
```

## How to Run

### Running the Backendh
# Make sure you're in the backend directory
cd backend

# Activate virtual environment (if using venv)
# Windows
venv\Scripts\activate

# Start the development server
python manage.py runserver
```

✅ **Backend will start at**: http://127.0.0.1:8000

**API Endpoints available:**
- `GET /api/invoices/` - List all invoices
- `POST /api/invoices/` - Create a new invoice
- `GET /api/invoices/{id}/` - Get invoice details
- `POST /api/invoices/{id}/payments/` - Add payment to invoice
- `POST /api/invoices/archive/` - Archive an invoice
- `POST /api/invoices/restore/` - Restore an archived invoice

**Admin Panel**: http://127.0.0.1:8000/admin/

### Running the Frontend
# Make sure you're in the frontend directory
cd frontend

# Start the development server
npm start
```

✅ **Frontend will open at**: http://localhost:3000 or http://localhost:3001

The browser will automatically open the application. If it doesn't, manually navigate to the URL shown in the terminal.

## Using the Application

### Creating an Invoice

1. Click **"+ New Invoice"** button on the dashboard
2. Fill in the following:
   - **Customer Name** (required) - e.g., "Acme Corp"
   - Invoice number (auto-generated)
   - Issue date (auto-filled with today)
   - Due date (auto-filled with 30 days from today)

3. Add line items:
   - **Description** - What you're billing for (e.g., "Web Development")
   - **Quantity** - Number of units (e.g., 1, 5, 10)
   - **Unit Price** - Price per unit in rupees (e.g., 50000)
   - Click **"+ Add Line Item"** to add more items

4. Click **"Create Invoice"** to save

### Viewing Invoices

1. Go to **Dashboard** to see all invoices with statistics
2. Click on any invoice to view details
3. View payment history and add payments
4. Track invoice status (DRAFT or PAID)

### Managing Admin Panel

1. Go to http://127.0.0.1:8000/admin/
2. Login with:
   - **Username**: `admin`
   - **Password**: `admin123`
3. Manage invoices, line items, and payments directly

⚠️ **SECURITY NOTE**: These default credentials are only for **local development**. If you plan to deploy this application:
- Change the admin password immediately
- Do NOT commit credentials to version control
- Use environment variables for sensitive information

## Project Structure

```
invoice-project/
├── backend/
│   ├── invoice_project/           # Django project settings
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── asgi.py
│   ├── invoices/                  # Main app
│   │   ├── models.py              # Invoice, InvoiceLine, Payment models
│   │   ├── views.py               # API views
│   │   ├── serializers.py         # DRF serializers
│   │   ├── urls.py                # API routes
│   │   ├── services.py            # Business logic
│   │   ├── validators.py          # Validation logic
│   │   ├── admin.py               # Admin panel config
│   │   └── migrations/            # Database migrations
│   ├── manage.py                  # Django management script
│   ├── db.sqlite3                 # SQLite database
│   └── requirement.txt            # Python dependencies
│
├── frontend/
│   ├── src/
│   │   ├── pages/                 # Page components
│   │   │   ├── Dashboard.jsx      # Invoice list & stats
│   │   │   ├── InvoiceDetails.jsx # Single invoice view
│   │   │   └── Home.jsx           # Redirect page
│   │   ├── components/            # Reusable components
│   │   │   ├── CreateInvoiceModal.jsx
│   │   │   ├── InvoiceHeader.jsx
│   │   │   ├── LineItemsTable.jsx
│   │   │   ├── TotalsSection.jsx
│   │   │   ├── PaymentsList.jsx
│   │   │   ├── AddPaymentModal.jsx
│   │   │   └── statusBadge.jsx
│   │   ├── services/              # API integration
│   │   │   ├── invoiceApi.js      # API calls
│   │   │   └── axiosInstance.js   # Axios config
│   │   ├── hooks/                 # Custom React hooks
│   │   │   └── useInvoice.js
│   │   ├── utils/                 # Utility functions
│   │   │   └── currencyFormatter.js
│   │   ├── styles/                # Global styles
│   │   │   └── style.css
│   │   ├── index.css              # Design system
│   │   ├── App.js                 # Main app component
│   │   └── index.js               # Entry point
│   ├── public/
│   │   ├── index.html
│   │   ├── manifest.json
│   │   └── robots.txt
│   ├── package.json               # Node dependencies
│   └── README.md
│
└── README.md                       # This file
```

## Troubleshooting

### Backend Issues

**Error: "can't find manage.py"**
- Make sure you're in the `backend` directory: `cd backend`

**Error: "ModuleNotFoundError"**
- Install requirements: `pip install -r requirement.txt`
- Activate virtual environment if using one

**Error: "Port 8000 already in use"**
- Kill the process: `python manage.py runserver 8001` (use different port)

### Frontend Issues

**Error: "npm: command not found"**
- Install Node.js from https://nodejs.org/

**Error: "Cannot find module"**
- Delete `node_modules` folder and reinstall: `rm -r node_modules && npm install`

**Port 3000 already in use**
- The app will automatically try port 3001 and higher

## API Examples

### Get All Invoices
```bash
curl http://127.0.0.1:8000/api/invoices/
```

### Create Invoice
```bash
curl -X POST http://127.0.0.1:8000/api/invoices/ \
  -H "Content-Type: application/json" \
  -d '{
    "invoiceNumber": "INV-001",
    "customerName": "John Doe",
    "issueDate": "2026-02-14",
    "dueDate": "2026-03-16"
  }'
```

### Add Payment
```bash
curl -X POST http://127.0.0.1:8000/api/invoices/1/payments/ \
  -H "Content-Type: application/json" \
  -d '{"amount": 5000}'
```

## Default Admin Credentials

- **URL**: http://127.0.0.1:8000/admin/
- **Username**: `admin`
- **Password**: `admin123`

⚠️ **IMPORTANT SECURITY WARNING**:

**These credentials are for LOCAL DEVELOPMENT ONLY**. 

❌ **DO NOT**:
- Use these credentials in production
- Commit credentials to version control (git)
- Share credentials in public repositories
- Expose the admin panel to the internet

✅ **DO**:
- Change the password after setup: `python manage.py changepassword admin`
- Use environment variables for production credentials
- Use strong, unique passwords in production
- Implement proper authentication and authorization
- Keep DEBUG = False in production

## Common Tasks

### Reset Database
```bash
# In backend directory
cd backend
Remove-Item db.sqlite3 -Force  # Windows
# Or: rm db.sqlite3  # macOS/Linux
python manage.py migrate
```

### Create New Admin User
```bash
python manage.py createsuperuser
```

### Run Backend on Different Port
```bash
python manage.py runserver 8001
```

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Review the browser console (F12) for error messages
3. Check backend terminal for server errors

## License

This project is provided as-is for educational and commercial use.

---

**Happy invoicing! 🎉**
=======
# invoice-billing-system
Full-Stack Invoice Management System built with React.js and Django REST Framework featuring invoice details, line items, payment tracking, and balance calculation.
>>>>>>> c21d940931ef7577d516e1bfe6a2aff61a8b03fa
