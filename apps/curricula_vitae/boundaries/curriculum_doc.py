from drf_spectacular.utils import (OpenApiExample, OpenApiResponse,
                                   extend_schema, inline_serializer)
from rest_framework import serializers

from apps.core.entities.enums.llm_models import LLMModels
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
            read_only=True,
            help_text="Código HTTP da resposta",
            default=200,
        ),
        "status": serializers.ChoiceField(
            choices=RequestStatus.choices,
            read_only=True,
            help_text=f"Status da requisição : {', '.join(RequestStatus.values)}",
            default=RequestStatus.SUCCESS,
        ),
        "path": serializers.CharField(
            read_only=True, help_text="Path da requisição", default="/api/v1/curriculum"
        ),
        "method": serializers.CharField(
            read_only=True, help_text="Método da requisição", default="POST"
        ),
    }


def get_error_response_fields():
    """
    Retorna os campos padrão para a resposta do endpoint.
    """
    return {
        "error": serializers.CharField(
            read_only=True,
            help_text="Mensagem de erro",
            default="Não foi possível enviar os dados referentes aos currículos, tente novamente mais tarde.",
        ),
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
                    name="Exemplo de sucesso, onde a query é 'Qual é o melhor candidato para uma vaga de desenvolvedor de inteligência artificial pleno?'",
                    value={
                        "code": 200,
                        "status": RequestStatus.SUCCESS,
                        "response": {
                            "ocr_model": OCRModels.EASYOCR,
                            "llm_model": LLMModels.LLAMA3_1,
                            "llm_response": "Considerando os currículos fornecidos, posso dizer que Bruno Tanabe é o melhor candidato para uma vaga de desenvolvedor de inteligência artificial pleno. Ele tem experiência significativa em desenvolvimento de soluções de IA, liderança de time e planejamento estratégico, além de habilidades técnicas fortes em áreas como Python, Java, Jupyter Notebook, Inteligência Artiﬁcial Generativa (IAG) e Aprendizado de Máquina (Machine Learning). Além disso, ele já liderou equipes e projetos complexos e tem experiência em desenvolvimento de softwares de negócios, o que sugere que ele pode adaptar-se facilmente a diferentes contextos e requisitos da empresa. Outros candidatos, como Ricardo Santos, apresentam habilidades técnicas relevantes, mas não têm experiência tão significativa em desenvolvimento de soluções de IA.",
                        },
                        "path": "/api/v1/curriculum",
                        "method": "POST",
                    },
                    response_only=True,
                    status_codes=["200"],
                ),
                OpenApiExample(
                    name="Exemplo de sucesso, onde a query não é informada",
                    value={
                        "code": 200,
                        "status": RequestStatus.SUCCESS,
                        "response": {
                            "ocr_model": OCRModels.EASYOCR,
                            "llm_model": LLMModels.LLAMA3_1,
                            "llm_response": "{'Bruno Tanabe': 'Engenheiro de Inteligência Artiﬁcial e BackEnd experiente, com habilidades em Python, Java, Inteligência Artiﬁcial Generativa, Aprendizado de Máquina e Processamento de Linguagem Natural. Possui experiência em liderança, desenvolvimento de sistemas de IA, chatbots e banco de dados.', 'Olívia Vieira': 'Engenheira mecânica com experiência em desenho mecânico e projetos de engenharia. Possui habilidades em software de projetos e inglês avançado.', 'Ricardo Santos': 'Engenheiro de software sênior com mais de 7 anos de experiência em desenvolvimento de códigos para negócios. Possui habilidades em liderança, trabalho em equipe e resolução de problemas. É vencedor do prêmio Faustino 2018 na categoria Cloud Services.'}",
                        },
                        "path": "/api/v1/curriculum",
                        "method": "POST",
                    },
                    response_only=True,
                    status_codes=["200"],
                ),
            ],
        ),
        400: OpenApiResponse(
            description="Erro de validação",
            response=inline_serializer(
                name="CurriculumAnalysisOutput",
                fields={
                    **get_error_response_fields(),
                    **get_default_response_fields(),
                },
            ),
            examples=[
                OpenApiExample(
                    name="Exemplo de erro onde a query tem mais de 256 caracteres e o request_id não é fornecido",
                    value={
                        "code": 400,
                        "status": RequestStatus.ERROR,
                        "response": {
                            "files": ["O campo 'files' é obrigatório."],
                            "query": ["O campo 'query' deve ter no máximo 256 caracteres."],
                            "request_id": ["O campo 'request_id' deve ser um UUID válido."],
                        },
                        "path": "/api/v1/curriculum",
                        "method": "POST",
                    },
                    response_only=True,
                    status_codes=["400"],
                ),
            ],
        ),
        500: OpenApiResponse(
            description="Erro interno do servidor",
            response=inline_serializer(
                name="CurriculumAnalysisOutput",
                fields={
                    **get_error_response_fields(),
                    **get_default_response_fields(),
                },
            ),
            examples=[
                OpenApiExample(
                    name="Exemplo de erro interno do servidor",
                    value={
                        "code": 500,
                        "status": RequestStatus.ERROR,
                        "response": {
                            "error": "Não foi possível enviar os dados referentes aos currículos, tente novamente mais tarde.",
                        },
                        "path": "/api/v1/curriculum",
                        "method": "POST",
                    },
                    response_only=True,
                    status_codes=["500"],
                ),
            ],
        ),
    },
)
