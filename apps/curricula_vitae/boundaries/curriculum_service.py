import uuid
from typing import List

from django.core.files.uploadedfile import UploadedFile
from django.utils import timezone

from apps.core.boundaries.interfaces.llm_service import LLMService
from apps.core.boundaries.interfaces.ocr_service import OCRService
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

    def __init__(self, ocr_model: OCRService, llm_provider: LLMService) -> None:
        self.ocr_model = ocr_model
        self.llm_provider = llm_provider

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
            # Verifica se o arquivo é um PDF
            if file.name.endswith(".pdf"):
                print("")
            else:
                curricula_txt += self.ocr_model.recognize_text(file)

        document_id = uuid.uuid4()

        extension, url = self.storage.upload_document(document_id, document_type, file)

        document = IdDocument.objects.create(
            id=document_id,
            name=name if name else None,
            type=document_type,
            url=url,
            extension=extension,
            sent_at=timezone.now(),
        )

        output_serializer = CurriculumCreateOutput(document)
        return document
