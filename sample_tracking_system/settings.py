import os
import dj_database_url
from pathlib import Path
from decouple import config, Csv

BASE_DIR = Path(__file__).resolve().parent.parent

# ── Security ──────────────────────────────────────────────────────────────────
SECRET_KEY = config('SECRET_KEY', default='django-insecure-h5m&_@5-1u#)_5=0(vcmx2$ru)hq2dc%9_hj!1!v!d!!p7rao+')

DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = ['sample-tracking-qzpe.onrender.com', '*']



# ── Apps ──────────────────────────────────────────────────────────────────────
INSTALLED_APPS = [
    'unfold',                           # must be before django.contrib.admin
    'unfold.contrib.filters',
    'unfold.contrib.forms',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sample',
]

# ── Middleware ────────────────────────────────────────────────────────────────
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',      # serve static files
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sample_tracking_system.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'sample_tracking_system.wsgi.application'

# ── Database ──────────────────────────────────────────────────────────────────
# Uses DATABASE_URL when set (Render/production); falls back to SQLite locally
_db_url = config('DATABASE_URL', default='')
if _db_url:
    DATABASES = {
        'default': dj_database_url.config(
            default=_db_url,
            conn_max_age=600,
        )
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME':   BASE_DIR / 'db.sqlite3',
        }
    }

# ── Password validation ───────────────────────────────────────────────────────
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ── Internationalisation ──────────────────────────────────────────────────────
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ── Static files ──────────────────────────────────────────────────────────────
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

STORAGES = {
    'default': {
        'BACKEND': 'django.core.files.storage.FileSystemStorage',
    },
    'staticfiles': {
        'BACKEND': 'whitenoise.storage.CompressedManifestStaticFilesStorage',
    },
}
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# ── Media files ───────────────────────────────────────────────────────────────
# Note: Render's filesystem is ephemeral on free tier.
# For persistent uploads, configure Cloudinary or AWS S3.
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ── Auth ──────────────────────────────────────────────────────────────────────
LOGIN_URL = '/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ── Unfold Admin Theme ────────────────────────────────────────────────────────
UNFOLD = {
    "SITE_TITLE": "Trecelo",
    "SITE_HEADER": "Trecelo Admin",
    "SITE_SUBHEADER": "Sample Tracking System",
    "SITE_URL": "/",
    "SITE_ICON": {
        "light": None,
        "dark": None,
    },
    "SITE_SYMBOL": "inventory_2",          # Google Material icon
    "SHOW_HISTORY": True,
    "SHOW_VIEW_ON_SITE": True,
    "THEME": "dark",                       # "light" | "dark" | None (auto)
    "COLORS": {
        "font": {
            "subtle-light":  "107 114 128",
            "subtle-dark":   "156 163 175",
            "default-light": "75 85 99",
            "default-dark":  "209 213 219",
            "important-light": "17 24 39",
            "important-dark":  "243 244 246",
        },
        "primary": {
            "50":  "239 246 255",
            "100": "219 234 254",
            "200": "191 219 254",
            "300": "147 197 253",
            "400": "96 165 250",
            "500": "59 130 246",
            "600": "37 99 235",
            "700": "29 78 216",
            "800": "30 64 175",
            "900": "30 58 138",
            "950": "23 37 84",
        },
    },
    "SIDEBAR": {
        "show_search": True,
        "show_all_applications": True,
        "navigation": [
            {
                "title": "Navigation",
                "separator": True,
                "items": [
                    {
                        "title": "Dashboard",
                        "icon": "dashboard",
                        "link": "/admin/",
                    },
                    {
                        "title": "Users",
                        "icon": "people",
                        "link": "/admin/auth/user/",
                    },
                ],
            },
            {
                "title": "Sample Management",
                "separator": True,
                "items": [
                    {
                        "title": "Samples",
                        "icon": "inventory_2",
                        "link": "/admin/sample/sample/",
                    },
                    {
                        "title": "Buyers",
                        "icon": "shopping_bag",
                        "link": "/admin/sample/buyer/",
                    },
                    {
                        "title": "Staff",
                        "icon": "badge",
                        "link": "/admin/sample/staffprofile/",
                    },
                ],
            },
            {
                "title": "Catalogue",
                "separator": True,
                "items": [
                    {
                        "title": "Brands",
                        "icon": "copyright",
                        "link": "/admin/sample/brand/",
                    },
                    {
                        "title": "Categories",
                        "icon": "category",
                        "link": "/admin/sample/category/",
                    },
                    {
                        "title": "GG",
                        "icon": "settings_input_component",
                        "link": "/admin/sample/gg/",
                    },
                    {
                        "title": "Challenge In",
                        "icon": "warning",
                        "link": "/admin/sample/challengein/",
                    },
                ],
            },
        ],
    },
    "TABS": [],
}



