"""
With these settings, tests run faster.
"""
import os

from .base import *  # noqa

env = environ.Env()

# Local Dev Env Flag
LOCAL_DEV_ENV = True


# DB
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(ROOT_DIR, "db.sqlite3"),
        "TEST": {
            # this gets you in-memory sqlite for faster testing
            "ENGINE": "django.db.backends.sqlite3",
        },
    }
}

# https://docs.djangoproject.com/en/dev/ref/settings/#test-runner
TEST_RUNNER = "django.test.runner.DiscoverRunner"

# CACHES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "",
    }
}

# PASSWORDS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#password-hashers
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

# TEMPLATES
# ------------------------------------------------------------------------------
TEMPLATES[-1]["APP_DIRS"] = False
TEMPLATES[-1]["OPTIONS"]["loaders"] = [  # type: ignore[index] # noqa F405
    (
        "django.template.loaders.cached.Loader",
        [
            "django.template.loaders.filesystem.Loader",
            "django.template.loaders.app_directories.Loader",
        ],
    )
]

# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"

# For testing
NINJA_EXTRA = {
    "PAGINATION_PER_PAGE": 20,
    "INJECTOR_MODULES": [],
    "PAGINATION_CLASS": "ninja_extra.pagination.LimitOffsetPagination",
    "THROTTLE_CLASSES": [
        "ninja_extra.throttling.AnonRateThrottle",
        "ninja_extra.throttling.UserRateThrottle",
    ],
    "NUM_PROXIES": None,
    "THROTTLE_RATES": {"user": None, "anon": None},
}

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["*"])
