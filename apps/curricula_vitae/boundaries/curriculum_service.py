import uuid
from typing import List

from django.core.files.uploadedfile import UploadedFile
from django.utils import timezone

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

    def __init__(self, storage: DocumentStorage) -> None:
        self.storage = storage

    def create(
        self,
        files: List[UploadedFile],
        name: str = None,
        document_type: DocumentType = DocumentType.UNDEFINED,
    ) -> IdDocument:
        """
        Cria um documento de identificação.
        """

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

        return document
