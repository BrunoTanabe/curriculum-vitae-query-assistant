from drf_spectacular.utils import (OpenApiExample, OpenApiResponse,
                                   extend_schema, inline_serializer)
from rest_framework import serializers

from apps.core.entities.enums.ocr_models import OCRModels
from apps.core.entities.enums.request_status import RequestStatus
from apps.curricula_vitae.entities.serializers.curriculum_create_input import \
    CurriculumCreateInput
from apps.curricula_vitae.entities.serializers.curriculum_create_output import \
    CurriculumCreateOutput

"""
    The Script id_document_doc.py.
    The id_document_doc.py script is responsible for

    @Author Bruno Tanabe
    @CreatedAt 2025-04-30
"""


def get_default_response_fields():
    """
    Retorna os campos padrão para a resposta do endpoint.
    """
    return {
        "code": serializers.IntegerField(
            read_only=True, help_text="Código HTTP da resposta"
        ),
        "status": serializers.ChoiceField(
            choices=RequestStatus.choices,
            read_only=True,
            help_text=f"Status da requisição : {', '.join(RequestStatus.values)}",
        ),
        "path": serializers.CharField(read_only=True, help_text="Path da requisição"),
        "method": serializers.CharField(read_only=True, help_text="Método da requisição"),
    }


curriculum_post = extend_schema(
    operation_id="curriculum_analysis_post",
    description=(
        "Este endpoint recebe múltiplos currículos (PDF, JPG, PNG), realiza OCR e análise via LLM para "
        "retornar um sumário individual ou uma resposta à query de recrutamento informada. "
        "Se a query for omitida, o sistema retornará apenas os sumários. "
        "Nenhum documento é armazenado, apenas logs mínimos são persistidos para auditoria."
    ),
    summary="Análise de currículos com OCR e LLM",
    tags=["Análise de Currículos"],
    request={
        "multipart/form-data": CurriculumCreateInput,
    },
    responses={
        200: OpenApiResponse(
            description="Resultado da análise dos currículos",
            response=inline_serializer(
                name="CurriculumAnalysisOutput",
                fields={
                    **CurriculumCreateOutput().get_fields(),
                    **get_default_response_fields(),
                },
            ),
            examples=[
                OpenApiExample(
                    name="Exemplo de sumário automático sem query",
                    value={
                        "code": 200,
                        "status": RequestStatus.SUCCESS,
                        "response": {
                            "model": OCRModels.EASYOCR,
                            "name": "RG do Bruno",
                            "type": DocumentType.RG,
                            "url": "https://bucket.s3.amazonaws.com/path/to/9596c0b9-77c8-4740-91dd-06d38a8dd045.png",
                            "sent_at": "2025-05-09T17:08:39.371122",
                        },
                        "path": "/api/v1/identification-document",
                        "method": "POST",
                    },
                    response_only=True,
                    status_codes=["201"],
                ),
                OpenApiExample(
                    name="Exemplo de sucesso utilizando um tipo não definido",
                    value={
                        "code": 200,
                        "status": RequestStatus.SUCCESS,
                        "response": {
                            "id": "9596c0b9-77c8-4740-91dd-06d38a8dd045",
                            "name": "",
                            "type": DocumentType.UNDEFINED,
                            "url": "https://bucket.s3.amazonaws.com/path/to/9596c0b9-77c8-4740-91dd-06d38a8dd045.png",
                            "sent_at": "2025-05-09T17:08:39.371122",
                        },
                    },
                    response_only=True,
                    status_codes=["201"],
                ),
            ],
        ),
    },
)

# https://drf-spectacular.readthedocs.io/en/latest/drf_spectacular.html#drf_spectacular.utils.extend_schema
