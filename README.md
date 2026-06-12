# Trecelo — Sample Tracking System

A full-featured, role-based web application built with **Django 6** for managing textile production samples, buyers, brands, and staff. Designed for garment and knitwear manufacturers who need a centralised system to track sample submissions from creation through approval.

**🔗 Live demo:** [https://sample-tracking-qzpe.onrender.com](https://sample-tracking-qzpe.onrender.com)

---

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [User Roles & Permissions](#user-roles--permissions)
- [Data Models](#data-models)
- [Getting Started](#getting-started)
- [Environment Variables](#environment-variables)
- [Usage Guide](#usage-guide)
- [Security Notes](#security-notes)
- [Production Deployment](#production-deployment)

---

## Features

### Sample Management
- Create, view, edit, and delete production samples with full technical specs
- Fields: Style Number, Sample Type, Color, Season, Size, Weight, Yarn Composition, GG, Status, Submission Date
- Attach front-part and back-part images per sample
- Upload unlimited **Challenge Part** images per sample with live preview
- Attach PDF / DOCX specification documents
- Lightbox gallery for full-size image viewing
- **Export** the current page to **PDF** or **Excel** with one click
- Rich-text description field powered by CKEditor 4

### Status Workflow
Samples move through four statuses with colour-coded badges:

| Status | Badge colour |
|--------|-------------|
| Draft | Grey |
| Pending | Amber |
| Approved | Green |
| Rejected | Red |

### Brand Management
- Create and manage brands with **Origin Country** (searchable select with 🏳️ emoji flags)
- Upload a **Brand Logo** per brand
- Brand logos are displayed as a live **auto-scrolling carousel** on the dashboard
- Brand list shows logo thumbnail, flag, and style count

### Buyer Management
- Create buyers with linked login credentials (username + password)
- Assign one or more brands to each buyer
- Buyers can only view samples that belong to their assigned brands

### Staff (Maker) Management
- Register staff members with employee ID, role, designation, NID, phone number
- Makers can only view samples they are assigned to

### Dashboard
- Stat cards: Total Samples, Buyers, Makers, Approved, Pending, Rejected, Draft
- **Doughnut** chart — Status distribution
- **Bar** chart — Samples by buyer
- **Line** chart — Monthly submission trend
- **Pie** chart — Samples by type
- **Brand logo carousel** — auto-sliding showcase of all brands with logos

### Admin Panel
- Powered by **django-unfold** (light theme)
- Full CRUD for all models via `/admin/`
- Custom sidebar navigation with Material icons

### UI & UX
- Tailwind CSS (Play CDN) — utility-first responsive design
- Fixed dark-navy sidebar with role badge and logout
- **Tom Select** — searchable single-select dropdowns for Brand, Category, GG, and Origin Country
- Custom multi-select dropdown (MSD) for Maker and Challenge In fields
- Status filter pills on the sample list
- Instant client-side search with 400 ms debounce
- Django flash messages on every create / update / delete action
- Empty-state prompts when lists have no data

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Django 6.0.4 |
| Language | Python 3.14 |
| Database | SQLite (dev) · PostgreSQL (prod via `dj-database-url`) |
| ORM | Django ORM |
| Image processing | Pillow 12.2 |
| Frontend | Tailwind CSS (Play CDN) · Font Awesome 6 (CDN) |
| Dropdowns | Tom Select 2.3.1 (CDN) |
| Rich text | CKEditor 4 (CDN) |
| Charts | Chart.js 4.4.2 (CDN) |
| Admin theme | django-unfold 0.97.0 |
| Static files | WhiteNoise 6.12 |
| PDF export | ReportLab |
| Excel export | openpyxl |
| Auth | Django built-in `django.contrib.auth` |
| Hosting | Render |

---

## Project Structure

```
sample_tracking_system/          ← project root
│
├── sample/                      ← main Django app
│   ├── migrations/              ← 22 migration files
│   ├── admin.py                 ← Unfold-themed admin with inlines
│   ├── apps.py
│   ├── context_processors.py    ← injects is_maker / is_buyer into all templates
│   ├── forms.py                 ← BuyerForm, StaffForm, SampleForm, BrandForm, …
│   ├── models.py                ← Brand, Buyer, StaffProfile, Sample, Category, GG, …
│   ├── urls.py                  ← all app URL patterns
│   └── views.py                 ← all views with role enforcement
│
├── sample_tracking_system/      ← Django project config
│   ├── settings.py              ← Unfold config, WhiteNoise, dj-database-url
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── templates/                   ← all HTML templates
│   ├── base.html                ← sidebar layout, topbar, Tailwind CDN
│   ├── login.html               ← split-panel login page
│   ├── dashboard.html           ← stat cards, charts, brand carousel
│   ├── sample_list.html         ← search, status filters, pagination, export
│   ├── sample_detail.html       ← images, lightbox, specs, challenge images
│   ├── form.html                ← shared create/edit form (Tom Select, CKEditor)
│   ├── brand_list.html          ← brand table with logo thumbnails and flag emojis
│   ├── buyer_list.html          ← buyer table with assigned brands
│   ├── staff_list.html
│   ├── lookup_list.html         ← shared table for Category, GG, Challenge In
│   └── confirm_delete.html
│
├── media/                       ← uploaded files (git-ignored on prod)
│   ├── brands/logos/
│   └── samples/
│       ├── front/
│       ├── back/
│       ├── challenge/
│       └── documents/
│
├── manage.py
├── requirements.txt
├── build.sh                     ← Render build script
├── render.yaml                  ← Render deployment config
└── README.md
```

---

## User Roles & Permissions

| Action | Buyer | Maker (Staff) | Superadmin |
|--------|:-----:|:-------------:|:----------:|
| View dashboard | ✅ | ✅ | ✅ |
| View samples (own brand / own maker) | ✅ | ✅ | ✅ |
| View all samples | ❌ | ❌ | ✅ |
| Create / edit / delete samples | ❌ | ✅ | ✅ |
| Export samples (PDF / Excel) | ✅ | ✅ | ✅ |
| View buyer list | ❌ | ❌ | ✅ |
| Create / edit / delete buyers | ❌ | ❌ | ✅ |
| View staff list | ❌ | ❌ | ✅ |
| Create / edit / delete staff | ❌ | ❌ | ✅ |
| Manage brands / categories / GG | ❌ | ❌ | ✅ |
| Access Django admin (`/admin/`) | ❌ | ❌ | ✅ |

> **Buyer access** is filtered at the query level — buyers only see samples whose brand matches one of their assigned brands.  
> **Maker access** is filtered at the query level — makers only see samples they are explicitly assigned to.

---

## Data Models

### `Brand`
| Field | Type | Notes |
|-------|------|-------|
| `name` | CharField(100) | Brand name |
| `origin` | CharField(100) | Country choice with 🏳️ emoji flag |
| `logo` | ImageField | Uploaded to `brands/logos/` |

### `Buyer`
| Field | Type | Notes |
|-------|------|-------|
| `user` | OneToOneField → User | Login credentials |
| `buyer_name` | CharField(100) | Display name |
| `brand` | ManyToManyField → Brand | Brands the buyer can view |

### `StaffProfile` (Maker)
| Field | Type | Notes |
|-------|------|-------|
| `user` | OneToOneField → User | Login credentials, `is_staff=True` |
| `emp_id` | CharField(50) | Unique employee ID |
| `role` | CharField(100) | e.g. "QC Inspector" |
| `designation` | CharField(100) | e.g. "Senior Officer" |
| `address` | TextField | |
| `nid` | CharField(30) | National ID number |
| `phone_number` | CharField(20) | |

### `Sample`
| Field | Type | Notes |
|-------|------|-------|
| `style_number` | CharField(100) | |
| `sample_type` | CharField(100) | |
| `color` | CharField(100) | |
| `season` | IntegerField | nullable |
| `status` | CharField | draft / pending / approved / rejected |
| `category` | ManyToManyField → Category | |
| `brand` | ManyToManyField → Brand | |
| `buyer` | ForeignKey → Buyer | nullable |
| `maker` | ManyToManyField → StaffProfile | |
| `front_part_image` | ImageField | upload to `samples/front/` |
| `back_part_image` | ImageField | upload to `samples/back/` |
| `documents` | FileField | upload to `samples/documents/` |
| `gg` | ManyToManyField → GG | Gauge specification |
| `size` | CharField(100) | |
| `weight` | CharField(100) | |
| `yarn_composition` | CharField(255) | |
| `description` | TextField | Rich text (CKEditor) |
| `challenge_in` | ManyToManyField → ChallengeIn | |
| `submission_date` | DateField | nullable |

### `ChallengeImage`
| Field | Type | Notes |
|-------|------|-------|
| `sample` | ForeignKey → Sample | CASCADE, `related_name='challenge_images'` |
| `image` | ImageField | upload to `samples/challenge/` |

### `Category`, `GG`, `ChallengeIn`
Simple lookup models with a single `name` / `title` CharField.

---

## Getting Started

### Prerequisites

- Python 3.10+
- pip
- Git

### 1 — Clone the repository

```bash
git clone https://github.com/jahidshawon19/trecelo.git
cd trecelo
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

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser and log in with your superuser credentials.

---

## Environment Variables

Create a `.env` file in the project root (already git-ignored):

```env
SECRET_KEY=your-very-secret-key-here
DEBUG=False
DATABASE_URL=postgres://user:password@host:5432/dbname
```

`settings.py` reads these automatically via `python-decouple` and `dj-database-url`. In development, all three have safe defaults so the `.env` file is optional.

---

## Usage Guide

### Login

Navigate to `/` — the split-panel login page.

| Account type | How to create |
|---|---|
| Superadmin | `python manage.py createsuperuser` |
| Maker (Staff) | Superadmin → Sidebar → Staff → Add Staff |
| Buyer | Superadmin → Sidebar → Buyers → Add Buyer |

---

### Managing Samples

1. Click **Samples** in the sidebar
2. Use the search bar or status filter pills to narrow results
3. Click **Add Sample** (superadmin / staff only) to open the form
4. Fill in specs; upload front/back images and challenge images
5. Select Brand, Category, GG using the searchable Tom Select dropdowns
6. Click **Save** — redirected to the sample detail page
7. Use **PDF** or **Excel** buttons to export the current page

---

### Managing Brands

1. Click **Brands** in the sidebar (superadmin only)
2. Click **Add Brand** — enter name, select origin country with flag emoji, optionally upload a logo
3. Brands with logos appear in the **carousel on the dashboard**

---

### Managing Buyers

1. Click **Buyers** in the sidebar (superadmin only)
2. Click **Add Buyer** — enter buyer name, username, password, and select one or more brands
3. The buyer logs in and sees only samples tagged with their assigned brands

---

### Managing Staff (Makers)

1. Click **Staff** in the sidebar (superadmin only)
2. Click **Add Staff** — fill in employee details, username, and password
3. The staff member logs in and sees only samples they are assigned to as a maker

---

## Security Notes

| Item | Status | Recommendation |
|---|---|---|
| `SECRET_KEY` | ⚠️ Default in dev | Move to `.env` / environment variable before deploying |
| `DEBUG` | ⚠️ `True` in dev | Set `DEBUG=False` in production |
| `ALLOWED_HOSTS` | ✅ Set for Render | Update if deploying elsewhere |
| CSRF protection | ✅ Enabled | All forms include `{% csrf_token %}` |
| Login required | ✅ Enforced | All views except `/` use `@login_required` |
| Role enforcement | ✅ Enforced | `@user_passes_test` on every privileged view |
| Query-level filtering | ✅ Enforced | Buyers and makers can only query their own data |
| SQL injection | ✅ Protected | Django ORM used throughout |
| XSS | ✅ Protected | Django auto-escaping on all templates |
| File uploads | ✅ Validated | `ImageField` validates image headers via Pillow |

---

## Production Deployment

This project is configured for **Render** out of the box via `render.yaml` and `build.sh`.

### Manual checklist

```bash
# 1. Set environment variables: SECRET_KEY, DEBUG=False, DATABASE_URL

# 2. Collect static files
python manage.py collectstatic --no-input

# 3. Apply migrations
python manage.py migrate

# 4. Start the server
gunicorn sample_tracking_system.wsgi:application
```

### Recommended production packages (already in requirements.txt)

```
gunicorn
psycopg2-binary
dj-database-url
python-decouple
whitenoise
```

---

## License

This project is for internal use. All rights reserved.

---

*Built with Django 6 · Tailwind CSS · Python 3.14 · Deployed on Render*
