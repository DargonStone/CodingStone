INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_summernote',
    'blog',
]


.
.
.
.
생략
.
.
.
.
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

SUMMERNOTE_CONFIG = {
    'attachment_filesize_limit': 5 * 1024 * 1024
}

