import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "local-study-secret-key")
DEBUG = os.environ.get("DJANGO_DEBUG", "1") == "1"
ALLOWED_HOSTS = [host.strip() for host in os.environ.get("DJANGO_ALLOWED_HOSTS", "*").split(",") if host.strip()]

INSTALLED_APPS = [
    "unfold",
    "unfold.contrib.filters",
    "unfold.contrib.forms",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "rest_framework",
    "content",
    "applications",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DB", "yelo"),
        "USER": os.environ.get("POSTGRES_USER", "yelo"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD", "yelo"),
        "HOST": os.environ.get("POSTGRES_HOST", "db"),
        "PORT": os.environ.get("POSTGRES_PORT", "5432"),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "az"
TIME_ZONE = "Asia/Baku"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
PUBLIC_BASE_URL = os.environ.get("PUBLIC_BASE_URL", "http://localhost:8000")
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CORS_ALLOWED_ORIGINS = [
    origin.strip()
    for origin in os.environ.get("CORS_ALLOWED_ORIGINS", "http://localhost:3000").split(",")
    if origin.strip()
]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [],
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.AllowAny"],
    "DEFAULT_RENDERER_CLASSES": ["rest_framework.renderers.JSONRenderer"],
}

UNFOLD = {
    "SITE_TITLE": "Yelo Study",
    "SITE_HEADER": "Yelo Study",
    "SITE_SYMBOL": "account_balance",
    "SHOW_HISTORY": True,
    "COLORS": {
        "primary": {
            "50": "255 251 235",
            "100": "254 243 199",
            "200": "253 230 138",
            "300": "252 211 77",
            "400": "251 191 36",
            "500": "234 179 8",
            "600": "202 138 4",
            "700": "161 98 7",
            "800": "133 77 14",
            "900": "113 63 18",
            "950": "66 32 6",
        },
    },
    "SIDEBAR": {
        "show_search": True,
        "navigation": [
            {
                "title": "Sayt",
                "separator": True,
                "items": [
                    {
                        "title": "Əmanətlər səhifəsi",
                        "icon": "savings",
                        "link": "/admin/content/depositspage/",
                    },
                    {
                        "title": "Kreditlər səhifəsi",
                        "icon": "payments",
                        "link": "/admin/content/loanspage/",
                    },
                    {
                        "title": "Kartlar səhifəsi",
                        "icon": "title",
                        "link": "/admin/content/cardspage/",
                    },
                    {
                        "title": "Keşbek səhifəsi",
                        "icon": "loyalty",
                        "link": "/admin/content/cashbackpage/",
                    },
                    {
                        "title": "Keşbek paketləri",
                        "icon": "redeem",
                        "link": "/admin/content/cashbackpack/",
                    },
                    {
                        "title": "Bannerlər",
                        "icon": "view_carousel",
                        "link": "/admin/content/banner/",
                    },
                    {
                        "title": "Məhsullar",
                        "icon": "credit_card",
                        "link": "/admin/content/product/",
                    },
                    {
                        "title": "Xəbərlər",
                        "icon": "newspaper",
                        "link": "/admin/content/newspost/",
                    },
                    {
                        "title": "Filiallar",
                        "icon": "location_on",
                        "link": "/admin/content/branch/",
                    },
                    {
                        "title": "Məzənnə",
                        "icon": "currency_exchange",
                        "link": "/admin/content/exchangerate/",
                    },
                    {
                        "title": "Müraciətlər",
                        "icon": "inbox",
                        "link": "/admin/applications/application/",
                    },
                    {
                        "title": "Onlayn növbə",
                        "icon": "confirmation_number",
                        "link": "/admin/applications/queueticket/",
                    },
                ],
            },
        ],
    },
}
