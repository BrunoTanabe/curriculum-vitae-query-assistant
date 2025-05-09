import os

from django.core.wsgi import get_wsgi_application

"""
    The Script wsgi.py.
    O arquivo wsgi.py é responsável por configurar o ambiente WSGI para o projeto Django.

    @Author Bruno Tanabe
    @CreatedAt 2025-05-07
"""

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "setup.settings")

application = get_wsgi_application()
