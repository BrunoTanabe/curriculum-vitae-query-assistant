from django.urls import path

from apps.curricula_vitae.boundaries.curriculum_api_view import \
    CurriculumAPIView

"""
The Script curriculum_url.py.
O arquivo curriculum_url.py define os padrões de URL para a API de documentos, mapeando o endpoint para a classe DocumentAPIView.

@Author Bruno Tanabe
@CreatedAt 2025-05-07
"""

urlpatterns = [
    path("curricula_vitae/", CurriculumAPIView.as_view(), name="curricula_vitae"),
]
