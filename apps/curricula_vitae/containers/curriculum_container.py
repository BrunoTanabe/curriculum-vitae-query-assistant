from dependency_injector import containers, providers
from django.conf import settings

from apps.core.boundaries.easyocr_service import EasyOCRService
from apps.core.boundaries.huggingface_service import HuggingFaceService
from apps.core.boundaries.pypdf_service import PyPDFService
from apps.curricula_vitae.boundaries.curriculum_service import \
    CurriculumService

"""
The Container curriculum_container.py.
A classe curriculum_container.py é um contêiner de injeção de dependências que fornece instâncias de serviços e componentes necessários para o funcionamento do aplicativo.

@Author Bruno Tanabe
@CreatedAt 2025-05-10
"""


# TODO: Adicionar suporte para outros provedores de OCR e LLM, melhorar a lógica de injeção de dependências
class CurriculumContainer(containers.DeclarativeContainer):
    """
    Container para o serviço de currículos.
    """
    wiring_config = containers.WiringConfiguration(
        modules=["apps.curricula_vitae.boundaries.curriculum_api_view"]
    )

    application_ocr_model = settings.APPLICATION_OCR_MODEL
    application_llm_provider = settings.APPLICATION_LLM_PROVIDER

    if (application_ocr_model == "easyocr") and (application_llm_provider == "huggingface"):
        easyocr_service = providers.Singleton(EasyOCRService)
        huggingface_service = providers.Singleton(HuggingFaceService)
        pypdf_service = providers.Singleton(PyPDFService)
        curriculum_service = providers.Factory(
            CurriculumService, ocr_service=easyocr_service, llm_service=huggingface_service, pdf_service=pypdf_service
        )
    else:
        print(
            f"Tipo de OCR ou LLM inválido: {application_ocr_model} ou {application_llm_provider}. "
            "Apenas 'easyocr' e 'huggingface' são suportados no momento."
        )
