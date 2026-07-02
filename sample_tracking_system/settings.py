import os
import dj_database_url
from pathlib import Path
from decouple import config, Csv

BASE_DIR = Path(__file__).resolve().parent.parent

# ── Security ──────────────────────────────────────────────────────────────────
SECRET_KEY = config('SECRET_KEY', default='django-insecure-h5m&_@5-1u#)_5=0(vcmx2$ru)hq2dc%9_hj!1!v!d!!p7rao+')

DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = ['sample-tracking-qzpe.onrender.com', '*']

# ── CSRF & Proxy ───────────────────────────────────────────────────────────────
# Required on Render (and any reverse-proxy host) so Django trusts the HTTPS
# origin forwarded by the proxy. Without this, Django sees requests as http://
# internally and rejects the CSRF token intermittently.
CSRF_TRUSTED_ORIGINS = config(
    'CSRF_TRUSTED_ORIGINS',
    default='https://sample-tracking-qzpe.onrender.com',
    cast=Csv(),
)

# Tell Django the real protocol when sitting behind Render's proxy
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Keep the CSRF cookie alive for the full session (default is per-browser-session)
CSRF_COOKIE_SAMESITE = 'Lax'
SESSION_COOKIE_SAMESITE = 'Lax'



# ── Apps ──────────────────────────────────────────────────────────────────────
INSTALLED_APPS = [
    'jazzmin',                          # must be before django.contrib.admin
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
    'sample.middleware.TopManagementReadOnlyMiddleware',
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
                'sample.context_processors.user_role',
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
TIME_ZONE = 'Asia/Dhaka'   # Bangladesh Standard Time (UTC+6)
USE_I18N = True
USE_TZ = True

# ── Static files ──────────────────────────────────────────────────────────────
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']

STORAGES = {
    'default': {
        'BACKEND': 'django.core.files.storage.FileSystemStorage',
    },
    'staticfiles': {
        'BACKEND': 'whitenoise.storage.CompressedStaticFilesStorage',
    },
}
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
# ── Media files ───────────────────────────────────────────────────────────────
# Note: Render's filesystem is ephemeral on free tier.
# For persistent uploads, configure Cloudinary or AWS S3.
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ── Auth ──────────────────────────────────────────────────────────────────────
LOGIN_URL = '/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ── Jazzmin Admin Theme ───────────────────────────────────────────────────────
JAZZMIN_SETTINGS = {
    # ── Branding ──────────────────────────────────────────────────────────────
    "site_title":        "Trecelo Admin",
    "site_header":       "Trecelo",
    "site_brand":        "Trecelo",
    "welcome_sign":      "Welcome to Trecelo Admin",
    "copyright":         "Trecelo",

    # Font Awesome icon for the browser tab
    "site_icon":         None,
    "site_logo":         None,
    "site_logo_classes": "img-circle",

    # ── Top nav search ────────────────────────────────────────────────────────
    "search_model": ["auth.user", "sample.sample", "sample.buyer"],

    # ── Top-right user menu links ─────────────────────────────────────────────
    "topmenu_links": [
        {"name": "Home",       "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Front-end",  "url": "/dashboard/",  "new_window": False},
        {"model": "auth.user"},
    ],

    # ── User menu (top-right avatar dropdown) ─────────────────────────────────
    "usermenu_links": [
        {"name": "Front-end", "url": "/dashboard/", "new_window": False, "icon": "fas fa-home"},
    ],

    # ── Sidebar ───────────────────────────────────────────────────────────────
    "show_sidebar":             True,
    "navigation_expanded":      True,
    "hide_apps":                [],
    "hide_models":              [],

    # Custom sidebar ordering
    "order_with_respect_to": [
        "auth",
        "sample",
        "sample.sample",
        "sample.buyer",
        "sample.staffprofile",
        "sample.topmanagement",
        "sample.generalcustomer",
        "sample.brand",
        "sample.category",
        "sample.gg",
        "sample.challengein",
        "sample.challengeimage",
    ],

    # ── Icons (Font Awesome 5) ────────────────────────────────────────────────
    "icons": {
        "auth":                       "fas fa-users-cog",
        "auth.user":                  "fas fa-user",
        "auth.group":                 "fas fa-users",
        "sample.sample":              "fas fa-box-open",
        "sample.buyer":               "fas fa-building",
        "sample.staffprofile":        "fas fa-id-badge",
        "sample.topmanagement":       "fas fa-user-tie",
        "sample.generalcustomer":     "fas fa-user-check",
        "sample.brand":               "fas fa-copyright",
        "sample.category":            "fas fa-tags",
        "sample.gg":                  "fas fa-tachometer-alt",
        "sample.challengein":         "fas fa-exclamation-triangle",
        "sample.challengeimage":      "fas fa-images",
    },
    "default_icon_parents":  "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    # ── UI tweaks ─────────────────────────────────────────────────────────────
    "related_modal_active":        True,
    "custom_css":                  "admin/css/custom.css",
    "custom_js":                   None,
    "use_google_fonts_cdn":        True,
    "show_ui_builder":             False,
    "changeform_format":           "horizontal_tabs",
    "changeform_format_overrides": {
        "auth.user":  "collapsible",
        "auth.group": "vertical_tabs",
    },
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text":      False,
    "footer_small_text":      False,
    "body_small_text":        False,
    "brand_small_text":       False,
    "brand_colour":           "navbar-dark",
    "accent":                 "accent-primary",
    "navbar":                 "navbar-dark",
    "no_navbar_border":       False,
    "navbar_fixed":           True,
    "layout_boxed":           False,
    "footer_fixed":           False,
    "sidebar_fixed":          True,
    "sidebar":                "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style":  False,
    "sidebar_nav_flat_style":    False,
    "theme":                  "default",
    "dark_mode_theme":        None,
    "button_classes": {
        "primary":   "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info":      "btn-info",
        "warning":   "btn-warning",
        "danger":    "btn-danger",
        "success":   "btn-success",
    },
}


