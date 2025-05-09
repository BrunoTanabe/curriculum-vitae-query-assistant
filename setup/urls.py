from django.shortcuts import redirect
from django.urls import include, path
from drf_spectacular.views import (SpectacularAPIView, SpectacularRedocView,
                                   SpectacularSwaggerView)

"""
    The Script urls.py.
    O arquivo urls.py é responsável por definir as rotas do projeto Django, mapeando URLs para as views correspondentes. Neste caso, ele inclui a rota para o painel de administração do Django.

    @Author Bruno Tanabe
    @CreatedAt 2025-05-07
"""


def redirect_to_docs(request):
    return redirect("docs")


urlpatterns = [
    # URLs gerais
    path("api/v1/", redirect_to_docs, name="api-root"),
    path("", redirect_to_docs, name="root-path"),
    # URLs da documentação
    path(
        "api/v1/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="docs",
    ),
    path("api/v1/download/", SpectacularAPIView.as_view(), name="schema"),
    path("api/v1/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    # URLs dos aplicativos
    # path(
    #    "api/v1/",
    #    include("apps.identification_document.urls.id_document_url"),
    # ),
]
