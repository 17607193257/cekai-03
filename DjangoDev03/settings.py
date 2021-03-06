"""
Django settings for DjangoDev03 project.

Generated by 'django-admin startproject' using Django 3.0.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^ggy(thzi#ky2@!8ccor_53+f=)^l=+(n3@v=qe#lf*2mkp(h+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #应用名.apps.应用名首字母大写Config（兼容性更好）或者直接写应用名
    'projects.apps.ProjectsConfig',
    'mypro.apps.MyproConfig',

    # 'interfaces'
    'interfaces.apps.InterfacesConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'DjangoDev03.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,"templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'DjangoDev03.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

#设置数据库的信息：
DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',  #django默认的数据库为sqlite3
        # 指定数据库引擎
        'ENGINE': 'django.db.backends.mysql',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        #指定数据库名称
        'NAME': 'dev03',
        #数据库用户名
        'USER':'root',
        'PASSWORD':'root', #公司电脑上的数据库密码
        # 'PASSWORD':'110120', #家里电脑上的数据库密码
        'HOST':'localhost',  #数据库主机域名或ip
        'PORT':3306 ,  #数据库的端口，端口为int类型
    }
    # #有多个数据库的场景：创建多个字典
    # 'mysql': {
    #     # 指定数据库引擎
    #     'ENGINE': 'django.db.backends.mysql',
    #     # 指定数据库名称
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    #     # 数据库用户名
    #     'USER': 'root',
    #     'PASSWORD': '',  # 数据库密码
    #     'HOST': '',  # 数据库主机、域名或ip
    #     'PORT': 3306,  # 端口为int类型
    #
    # }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
