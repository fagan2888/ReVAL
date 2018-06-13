import sys

import django
from django.conf import settings
from django.test.utils import get_runner

SETTINGS = {"DATABASES": {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'data_ingest',
    }},
    "INSTALLED_APPS": [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'data_ingest',
        'data_ingest.tests'
]
}

settings.configure(**SETTINGS)
django.setup()

TestRunner = get_runner(settings)

test_runner = TestRunner(verbosity=1, interactive=True)
failures = test_runner.run_tests(['data_ingest',])
sys.exit(failures)
