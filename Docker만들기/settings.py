SECRET_KEY = os.environ.get('SECRET_KEY', '---- 시크릿 키 번호를 넣어주세요----')



DEBUG = int(os.environ.get('DEBUG', 1))

if os.environ.get('DJANGO_ALLOWED_HOSTS'):
    ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS').split(' ')
else:
    ALLOWED_HOSTS = []
