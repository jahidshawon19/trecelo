# Trecelo — Production Sample Tracking System

A full-featured, role-based web application built with **Django 6** for managing textile production samples, buyers, and staff. Designed for garment and knitwear manufacturers who need a centralised system to track sample submissions from creation to delivery.

---

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [User Roles & Permissions](#user-roles--permissions)
- [Data Models](#data-models)
- [Getting Started](#getting-started)
- [Environment Setup](#environment-setup)
- [Running the Project](#running-the-project)
- [Usage Guide](#usage-guide)
- [Screenshots](#screenshots)
- [Security Notes](#security-notes)
- [Production Deployment](#production-deployment)

---

## Features

### Core
- **Product Sample Management** — Create, view, edit, and delete product samples with full technical specifications
- **Multiple Image Upload** — Attach unlimited images per product with a live-preview uploader and lightbox gallery
- **Document Attachment** — Upload PDF/DOCX specification documents per product
- **Buyer Management** — Create and manage buyer accounts with linked login credentials
- **Staff Management** — Register staff members with employee ID, role, designation, and contact info

### Access Control
- **Three-tier role system** — Superadmin, Staff, and Buyer with strictly enforced view-level permissions
- **Buyers see only their own products** — filtered automatically at the query level
- **Staff can manage products and buyers** — but cannot manage other staff members
- **Superadmin has full access** — including staff creation and deletion

### UI & UX
- **Sidebar dashboard layout** — fixed 260px dark-navy sidebar, sticky topbar with role badge and logout
- **Split-panel login page** — branded left panel with feature list, clean right-panel form
- **Client-side product search** — instant filter on the product list without page reload
- **Lightbox image viewer** — click any gallery thumbnail to open full-size in a modal
- **Django flash messages** — success and error alerts on every create / update / delete action
- **Responsive design** — collapsible sidebar with hamburger toggle on mobile
- **Empty states** — contextual prompts when lists have no data

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django 6.0.4 |
| Language | Python 3.14 |
| Database | SQLite (dev) / PostgreSQL (prod) |
| Image processing | Pillow 12.2 |
| Frontend | Bootstrap 5.3.2 + FontAwesome 6.4.0 (CDN) |
| Static files | WhiteNoise 6.12 |
| Auth | Django built-in `django.contrib.auth` |

---

## Project Structure

```
sample_tracking_system/          ← project root
│
├── sample/                      ← main Django app
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   └── 0002_remove_product_back_part_image_and_more.py
│   ├── admin.py                 ← ProductImage TabularInline, ProductAdmin
│   ├── apps.py
│   ├── forms.py                 ← BuyerForm, StaffForm, ProductForm, MultipleImageField
│   ├── models.py                ← Buyer, StaffProfile, Product, ProductImage
│   ├── tests.py
│   ├── urls.py                  ← all app URL patterns
│   └── views.py                 ← all views with messages & select_related
│
├── sample_tracking_system/      ← Django project config
│   ├── settings.py
│   ├── urls.py                  ← root URLconf + media serving
│   ├── asgi.py
│   └── wsgi.py
│
├── templates/                   ← all HTML templates
│   ├── base.html                ← sidebar layout, topbar, messages
│   ├── login.html               ← standalone split-panel login
│   ├── product_list.html        ← stats card, search, table
│   ├── product_detail.html      ← gallery, lightbox, upload modal, specs
│   ├── staff_list.html
│   ├── buyer_list.html
│   ├── form.html                ← shared create/edit form
│   └── confirm_delete.html      ← delete confirmation card
│
├── media/                       ← uploaded files (git-ignored)
│   └── products/
│       ├── images/
│       └── documents/
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## User Roles & Permissions

| Action | Buyer | Staff | Superadmin |
|---|:---:|:---:|:---:|
| View own products | ✅ | ✅ | ✅ |
| View all products | ❌ | ✅ | ✅ |
| Create / edit / delete products | ❌ | ✅ | ✅ |
| Upload / delete product images | ❌ | ✅ | ✅ |
| View buyer list | ❌ | ✅ | ✅ |
| Create / edit / delete buyers | ❌ | ✅ | ✅ |
| View staff list | ❌ | ❌ | ✅ |
| Create / edit / delete staff | ❌ | ❌ | ✅ |
| Access Django admin | ❌ | ❌ | ✅ |

---

## Data Models

### `Buyer`
| Field | Type | Notes |
|---|---|---|
| `user` | OneToOneField → User | Login credentials |
| `buyer_name` | CharField(100) | Display name |

### `StaffProfile`
| Field | Type | Notes |
|---|---|---|
| `user` | OneToOneField → User | Login credentials, `is_staff=True` |
| `emp_id` | CharField(50) | Unique employee ID |
| `role` | CharField(100) | e.g. "QC Inspector" |
| `designation` | CharField(100) | e.g. "Senior Officer" |
| `address` | TextField | |
| `nid` | CharField(30) | National ID number |
| `phone_number` | CharField(20) | |

### `Product`
| Field | Type | Notes |
|---|---|---|
| `product_name` | CharField(100) | |
| `buyer` | ForeignKey → Buyer | nullable |
| `maker` | ForeignKey → StaffProfile | nullable, `SET_NULL` |
| `documents` | FileField | upload to `products/documents/` |
| `gg` | TextField | Gauge specification |
| `end_ply` | IntegerField | |
| `weight` | FloatField | |
| `yarn_composition` | TextField | |
| `description` | TextField | |
| `challenge_in` | TextField | Production challenges |
| `submission_date` | DateField | nullable |
| `knitting_smv` | IntegerField | Standard minute value |
| `linking_smv` | IntegerField | Standard minute value |

### `ProductImage`
| Field | Type | Notes |
|---|---|---|
| `product` | ForeignKey → Product | `related_name='images'`, CASCADE |
| `image` | ImageField | upload to `products/images/` |
| `caption` | CharField(120) | optional |
| `uploaded_at` | DateTimeField | auto |

---

## Getting Started

### Prerequisites

- Python 3.10 or higher
- pip
- Git

### 1 — Clone the repository

```bash
git clone https://github.com/jahidshawon19/sample-tracking-system.git
cd sample-tracking-system
```

### 2 — Create and activate a virtual environment

```bash
python -m venv venv

# macOS / Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3 — Install dependencies

```bash
pip install -r requirements.txt
```

### 4 — Apply migrations

```bash
python manage.py migrate
```

### 5 — Create a superadmin account

```bash
python manage.py createsuperuser
```

### 6 — Run the development server

```bash
python manage.py runserver
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

---

## Environment Setup

For development the defaults in `settings.py` work out of the box. For any shared or production environment, move sensitive values into environment variables.

Create a `.env` file in the project root (it is git-ignored):

```env
DJANGO_SECRET_KEY=your-very-secret-key-here
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
```

Then update `settings.py`:

```python
import os

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'fallback-dev-only-key')
DEBUG = os.environ.get('DJANGO_DEBUG', 'True') == 'True'
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', 'localhost').split(',')
```

---

## Running the Project

### Development server

```bash
python manage.py runserver
```

### Create staff member via Django admin

1. Go to [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
2. Log in with your superuser credentials
3. Or use the **Staff** section in the app sidebar (superadmin only)

### Run system checks

```bash
python manage.py check
```

### Create new migrations after model changes

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## Usage Guide

### Login

Navigate to `/` — you will see the split-panel login page.

| Account type | Created by |
|---|---|
| Superadmin | `python manage.py createsuperuser` |
| Staff | Superadmin via the Staff section |
| Buyer | Staff or Superadmin via the Buyers section |

---

### Managing Products (Staff / Superadmin)

1. Click **Products** in the sidebar
2. Click **Add Product** to open the product form
3. Fill in product details, technical specifications, and attach a document if needed
4. Select one or more images using the **Product Images** file picker (hold `Ctrl`/`Cmd` to select multiple)
5. Click **Save** — you are redirected to the product detail page

**To add more images later:**
- Open the product detail page
- Click **Add Images** (top-right of the Images card)
- Select images in the modal and click **Upload & Save**

**To remove an image:**
- On the product detail page, click the **×** button on any thumbnail

---

### Managing Buyers (Staff / Superadmin)

1. Click **Buyers** in the sidebar
2. Click **Add Buyer** — enter a buyer name, username, and password
3. The buyer can then log in and view only the products assigned to them

---

### Managing Staff (Superadmin only)

1. Click **Staff** in the sidebar
2. Click **Add Staff** — fill in employee details, username, and password
3. The staff member gets `is_staff = True` automatically, granting access to product and buyer management

---

## Security Notes

| Item | Status | Recommendation |
|---|---|---|
| `SECRET_KEY` hardcoded | ⚠️ Dev only | Move to environment variable before deploying |
| `DEBUG = True` | ⚠️ Dev only | Set `DEBUG = False` in production |
| `ALLOWED_HOSTS = []` | ⚠️ Dev only | Set to your domain(s) in production |
| CSRF protection | ✅ Enabled | All forms use `{% csrf_token %}` |
| Login required | ✅ Enforced | All views except login use `@login_required` |
| Role enforcement | ✅ Enforced | `@user_passes_test` on every sensitive view |
| SQL injection | ✅ Protected | Django ORM used throughout |
| XSS | ✅ Protected | Django auto-escaping enabled |
| File uploads | ✅ Pillow validated | `ImageField` validates image headers |

---

## Production Deployment

### Checklist

```bash
# 1. Set environment variables (SECRET_KEY, DEBUG=False, ALLOWED_HOSTS)

# 2. Collect static files
python manage.py collectstatic

# 3. Use a production database (PostgreSQL recommended)
# Add to settings.py:
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.environ.get('DB_NAME'),
#         'USER': os.environ.get('DB_USER'),
#         'PASSWORD': os.environ.get('DB_PASSWORD'),
#         'HOST': os.environ.get('DB_HOST', 'localhost'),
#         'PORT': os.environ.get('DB_PORT', '5432'),
#     }
# }

# 4. Run migrations on production database
python manage.py migrate

# 5. Serve with Gunicorn + Nginx
pip install gunicorn
gunicorn sample_tracking_system.wsgi:application --bind 0.0.0.0:8000
```

### Recommended packages for production

```bash
pip install gunicorn psycopg2-binary python-decouple
```

---

## License

This project is for internal use. All rights reserved.

---

*Built with Django 6 · Bootstrap 5 · Python 3.14*
