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
        allow_blank=False,
        allow_null=False,
        required=True,
        default=OCRModels.EASYOCR,
        help_text=f"Modelo de OCR utilizado: {', '.join(OCRModels.values)}",
        error_messages={
            "invalid_choice": f"O campo 'ocr_model' deve ter um dos seguintes valores: {', '.join(OCRModels.values)}.",
            f"blank": "O campo 'ocr_model' não pode estar vazio.",
            f"null": "O campo 'ocr_model' não pode ser nulo.",
        },
    )

    llm_model = serializers.ChoiceField(
        choices=LLMModels.choices,
        allow_blank=False,
        allow_null=False,
        required=True,
        default=LLMModels.DEEPSEEKV3,
        help_text=f"Modelo de LLM utilizado: {', '.join(LLMModels.values)}",
        error_messages={
            "invalid_choice": f"O campo 'llm_model' deve ter um dos seguintes valores: {', '.join(LLMModels.values)}.",
            f"blank": "O campo 'llm_model' não pode estar vazio.",
            f"null": "O campo 'llm_model' não pode ser nulo.",
        },
    )

    llm_response = serializers.CharField(
        allow_blank=False,
        allow_null=False,
        required=True,
        default="Não foi possível enviar os dados referentes aos currículos, tente novamente mais tarde.",
        help_text="Resposta do modelo de inteligência artificial.",
        error_messages={
            f"blank": "O campo 'llm_response' não pode estar vazio.",
            f"null": "O campo 'llm_response' não pode ser nulo.",
        },
    )
