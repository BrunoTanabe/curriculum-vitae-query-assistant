from dependency_injector import containers, providers
from django.conf import settings

from apps.core.boundaries import easyocr_service
from apps.core.boundaries.easyocr_service import EasyOCRService
from apps.core.entities.enums.ocr_models import OCRModels
from apps.curricula_vitae.boundaries.curriculum_service import \
    CurriculumService

"""
The Container curriculum_container.py.
A classe curriculum_container.py é um contêiner de injeção de dependências que fornece instâncias de serviços e componentes necessários para o funcionamento do aplicativo.

@Author Bruno Tanabe
@CreatedAt 2025-05-10
"""


class CurriculumContainer(containers.DeclarativeContainer):
    """
    Container para o serviço de currículos.
    """

    wiring_config = containers.WiringConfiguration(
        modules=["apps.curricula_vitae.boundaries.curriculum_api_view"]
    )

    application_ocr_model = settings.APPLICATION_OCR_MODEL

    if application_ocr_model == "easyocr":
        easyocr_service = providers.Singleton(EasyOCRService)
        curriculum_service = providers.Factory(CurriculumService, ocr_model=easyocr_service)
    else:
        raise ValueError(
            f"Tipo de modelo de OCR inválido: {application_ocr_model}. "
            f"Os modelos suportados são: {OCRModels.values}."
        )
