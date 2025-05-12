from rest_framework import serializers

from apps.core.entities.enums.llm_models import LLMModels
from apps.core.entities.enums.ocr_models import OCRModels

"""
The Serializer curriculum_create_output.py.
O serializador curriculum_create_output.py é responsável por transformar o formato de saída após o envio dos currículos.

@Author Bruno Tanabe
@CreatedAt 2025-05-08
"""


class CurriculumCreateOutput(serializers.Serializer):
    """
    Serializer para saída de dados após a criação de um currículo.
    """

    ocr_model = serializers.ChoiceField(
        choices=OCRModels.choices,
        read_only=True,
        help_text=f"Modelo de OCR utilizado: {', '.join(OCRModels.values)}",
    )

    llm_model = serializers.ChoiceField(
        choices=LLMModels.choices,
        read_only=True,
        help_text=f"Modelo de LLM utilizado: {', '.join(LLMModels.values)}",
    )

    llm_response = serializers.CharField(
        read_only=True, help_text="Resposta do modelo de inteligência artificial."
    )

    class Meta:
        fields = ["ocr_model", "llm_model", "llm_response"]
