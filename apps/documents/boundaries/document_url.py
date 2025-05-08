"""
The Script document_url.py.
O arquivo document_url.py define os padrões de URL para a API de documentos, mapeando o endpoint para a classe DocumentAPIView.

@Author Bruno Tanabe
@CreatedAt 2025-05-07
"""

urlpatterns = [
    path("documents/", DocumentAPIView.as_view(), name="documents"),
]