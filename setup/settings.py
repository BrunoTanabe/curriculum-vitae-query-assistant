import os
from pathlib import Path

import environ
from mongoengine import connect

"""
    The Script settings.py.
    O arquivo settings.py é responsável por configurar as definições do projeto Django, incluindo o diretório base, a chave secreta, as configurações de depuração, os aplicativos instalados, o middleware, as configurações de banco de dados e outras opções essenciais para o funcionamento do projeto.

    @Author Bruno Tanabe
    @CreatedAt 2025-05-07
"""

env = environ.Env(
    DEBUG=(bool, False),
)

BASE_DIR = Path(__file__).resolve().parent.parent

environ.Env.read_env(os.path.join(BASE_DIR, ".env"), parse_comments=False, overwrite=True)

env.prefix = "DJANGO_"
SECRET_KEY = env.str("SECRET_KEY")
DEBUG = env.str("DEBUG")

env.prefix = "APPLICATION_"
APPLICATION_LLM_PROVIDER = env.str("LLM_PROVIDER")
APPLICATION_OCR_MODEL = env.str("OCR_MODEL")
APPLICATION_LLM_MODEL = env.str("LLM_MODEL")

env.prefix = "HUGGINGFACE_"
HUGGINGFACE_ACCESS_TOKEN = env.str("ACCESS_TOKEN")

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    # Aplicativos nativos do Django
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Aplicativos de terceiros
    "rest_framework",
    "drf_spectacular",
    "corsheaders",
    # Aplicativos locais
    "apps.curricula_vitae",
]

REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_RENDERER_CLASSES": [
        "apps.core.controls.standard_response_renderer.StandardResponseRenderer",
    ],
    "EXCEPTION_HANDLER": "apps.core.controls.standard_exception_handler.standard_exception_handler",
}

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "apps.core.controls.standard_response_middleware.StandardResponseMiddleware",
]

ROOT_URLCONF = "setup.urls"

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

WSGI_APPLICATION = "setup.wsgi.application"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

env.prefix = "MONGODB_"
MONGODB_USERNAME = env.str("USERNAME")
MONGODB_PASSWORD = env.str("PASSWORD")
MONGODB_DATABASE_NAME = env.str("DATABASE_NAME")
MONGODB_HOST = env.str("HOST")
MONGODB_PORT = env.int("PORT")
MONGODB_AUTHENTICATION_SOURCE = env.str("AUTHENTICATION_SOURCE")

connect(
    db=MONGODB_DATABASE_NAME,
    username=MONGODB_USERNAME,
    password=MONGODB_PASSWORD,
    host=MONGODB_HOST,
    port=MONGODB_PORT,
    authentication_source=MONGODB_AUTHENTICATION_SOURCE,
)

LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Sao_Paulo"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

SPECTACULAR_SETTINGS = {
    "TITLE": "Curriculum Vitae Query Assistant",
    "DESCRIPTION": "Ferramenta com tecnologia de IA que extrai e resume currículos (PDF, JPEG/PNG) usando OCR e LLMs, responde a consultas sobre adequação à vaga e registra todos os dados de uso (sem armazenar documentos). Desenvolvido para fluxos de trabalho de contratação eficientes. Rápido, auditável e totalmente Dockerizado com a API Swagger.",
    "VERSION": "1.0.0",
    "COMPONENT_SPLIT_REQUEST": True,
    "DEFAULT_GENERATOR_CLASS": "drf_spectacular.generators.SchemaGenerator",
    "CAMELIZE_NAMES": True,
    "SORT_OPERATIONS": True,
    "COMPONENT_NO_READ_ONLY_REQUIRED": False,
    "SWAGGER_UI_SETTINGS": {
        "deepLinking": True,
        "displayRequestDuration": True,
        "filter": True,
    },
}
