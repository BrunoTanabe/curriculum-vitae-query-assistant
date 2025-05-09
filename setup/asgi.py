import os

from django.core.asgi import get_asgi_application

"""
    The Script asgi.py.
    O arquivo asgi.py é o ponto de entrada para servidores ASGI, como Daphne ou Uvicorn.

    @Author Bruno Tanabe
    @CreatedAt 2025-05-07
"""

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "setup.settings")

application = get_asgi_application()
