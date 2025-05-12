import json
from datetime import datetime

from django.conf import settings

from apps.core.boundaries.interfaces.llm_service import LLMService
from apps.core.boundaries.interfaces.ocr_service import OCRService
from apps.core.boundaries.pypdf_service import PyPDFService
from apps.curricula_vitae.entities.models.curriculum import Curriculum

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

    def __init__(
        self, ocr_service: OCRService, llm_service: LLMService, pdf_service: PyPDFService
    ) -> None:
        self.ocr_service = ocr_service
        self.llm_service = llm_service
        self.pdf_service = pdf_service

    def create(
        self,
        data,
    ):
        """
        Processa o upload de arquivos de currículo e a pergunta e retorna o resultado.
        Se a pergunta não for fornecida, retorna um resumo dos currículos.
        """

        curricula_txt = ""

        files = data["files"]

        for file in files:
            curricula_txt += "{$$\n"
            curricula_txt += f"CURRÍCULO: ({file.name})\n"

            if file.content_type == "application/pdf":
                curricula_txt += self.pdf_service.extract_text(file)
            else:
                curricula_txt += self.ocr_service.recognize_text(file)

            curricula_txt += "\n$$}"

        if not data.get("query"):
            llm_response = self.llm_service.curricula_summarization(curricula=curricula_txt)
            try:
                llm_response = json.loads(llm_response)
            except Exception:
                llm_response = llm_response
        else:
            llm_response = self.llm_service.curricula_analysis(
                curricula=curricula_txt,
                query=str(data["query"]),
            )

        result_str = (
            llm_response
            if isinstance(llm_response, str)
            else json.dumps(llm_response, ensure_ascii=False)
        )
        Curriculum(
            request_id=data["request_id"],
            user_id=data["user_id"],
            timestamp=datetime.now(),
            query=data.get("query", ""),
            result=result_str,
        ).save()

        return {
            "ocr_model": settings.APPLICATION_OCR_MODEL,
            "llm_model": settings.APPLICATION_LLM_MODEL,
            "llm_response": llm_response,
        }
