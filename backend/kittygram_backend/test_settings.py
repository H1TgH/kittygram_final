import sys
from os.path import abspath, dirname
from pathlib import Path

sys.path.insert(0, dirname(dirname(abspath(__file__))))

try:
    from kittygram_backend import settings as base_settings
except ImportError:
    import sys
    sys.path.append(dirname(dirname(dirname(abspath(__file__)))))
    from kittygram_backend import settings as base_settings

for attr in dir(base_settings):
    if not attr.startswith('_'):
        globals()[attr] = getattr(base_settings, attr)

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]

SECRET_KEY = 'test-secret-key'
DEBUG = False
ALLOWED_HOSTS = ['testserver']
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
