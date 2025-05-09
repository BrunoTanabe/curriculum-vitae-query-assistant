from rest_framework import serializers

from apps.identification_document.entities.models import IdDocument

"""
The Serializer curriculum_create_output.py.
O serializador curriculum_create_output.py é responsável ptransformar o formato de saída após o envio dos currículos.

@Author Bruno Tanabe
@CreatedAt 2025-05-08
"""


class CurriculumCreateOutput(serializers.Serializer):
    """
    Serializer para saída de dados após a criação de um documento de identificação.
    """

    pass
