
SECRET_KEY = 'c&amp;2sr12q0^g^+epf5g#-lm6+3a(trr5+&amp;v_47jwv4!87oj4k+l'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'app_name.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'face_off',
)

ROOT_URLCONF = 'face_off.urls'

SITE_ID = 1
