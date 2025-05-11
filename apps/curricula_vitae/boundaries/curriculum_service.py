import uuid

from django.conf import settings
from django.utils import timezone

from apps.core.boundaries.interfaces.llm_service import LLMService
from apps.core.boundaries.interfaces.ocr_service import OCRService
from apps.core.boundaries.pypdf_service import PyPDFService
from apps.curricula_vitae.entities.serializers.curriculum_create_output import \
    CurriculumCreateOutput

"""
The Service id_document_service.py.
The id_document_service.py service is responsible for handling operations related to identification documents, such as uploading and processing documents, and managing their metadata.

@Author Bruno Tanabe
@CreatedAt 2025-05-08
"""


class CurriculumService:
    """
    Serviço de criação de documentos de identificação.
    """

    def __init__(self, ocr_service: OCRService, llm_service: LLMService, pdf_service: PyPDFService) -> None:
        self.ocr_service = ocr_service
        self.llm_service = llm_service
        self.pdf_service = pdf_service

    def create(
            self,
            data,
    ) -> CurriculumCreateOutput:
        """
        Processa o upload de arquivos de currículo e a pergunta e retorna o resultado.
        Se a pergunta não for fornecida, retorna um resumo dos currículos.
        """

        curricula_txt = ""

        for file in data["files"]:
            curricula_txt = "{$$\n"

            curricula_txt += f"CURRÍCULO {data['files'].index(file) + 1} ({file.name}):\n"

            if file.content_type == "application/pdf":
                curricula_txt += self.pdf_service.extract_text(file)
            else:  # não preciso de mais nenhuma verificação, o tipo de arquivo já foi validado no serializer
                curricula_txt += self.ocr_service.recognize_text(file)

            curricula_txt += "\n$$}"

        if not data.get("query"):
            llm_response = self.llm_service.curricula_summarization(curricula=curricula_txt)
        else:
            llm_response = self.llm_service.curricula_analysis(
                curricula=curricula_txt,
                query=str(data["query"]),
            )

        return CurriculumCreateOutput(
            ocr_model=settings.APPLICATION_OCR_MODEL,
            llm_model=settings.APPLICATION_LLM_MODEL,
            llm_response=llm_response,
        )
