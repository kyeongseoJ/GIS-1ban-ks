from .base import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/
# 보안 정보를 읽어오는 함수 설정
# 경로 알기 위해서 포테이너 마리아디비 커넥트해서 확인할 수 있다. 혹은 공식문서 참고

def read_secrets(secret_name):
    file = open('/run/secrets/'+ secret_name)
    secret = file.read()
    secret = secret.rstrip().lstrip()
    file.close()
    return secret
    
# SECURITY WARNING: keep the secret key used in production secret!
# .yml파일에서 가져오는 시크릿 키 사용
SECRET_KEY =read_secrets('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': read_secrets('MARIADB_USER'),
        'PASSWORD': read_secrets('MARIADB_PASSWORD'),
        'HOST': 'mariadb',
        'PORT': '3306',
    }
}



