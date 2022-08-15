STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '_static/')
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '_media/')

SUMMERNOTE_CONFIG = {
    'attachment_filesize_limit': 5 * 1024 * 1024
