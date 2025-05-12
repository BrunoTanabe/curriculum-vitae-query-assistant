import re

from PyPDF2 import PdfReader

from apps.core.boundaries.interfaces.pdf_service import PDFService

"""
The Service pypdf_service.py.
O service pypdf_service.py é responsável por extrair texto de arquivos PDF, permitindo a leitura e manipulação do conteúdo dos documentos.
Ele utiliza a biblioteca PyPDF2 para realizar a extração de texto de forma eficiente e estruturada, facilitando o processamento posterior dos dados extraídos.

@Author Bruno Tanabe
@CreatedAt 2025-05-11
"""


class PyPDFService(PDFService):

    def __init__(self):
        """
        Inicializa o serviço PyPDFService.
        """
        return

    def extract_text(self, file):
        reader = PdfReader(file)
        raw_text = ""

        for page in reader.pages:
            text = page.extract_text()
            if text:
                raw_text += text + "\n"

        return self._normalize_text(raw_text)

    def _normalize_text(self, text):

        text = re.sub(r"-\n", "", text)
        text = re.sub(r"(?<!\n)\n(?!\n)", " ", text)
        text = re.sub(r"\n{2,}", "\n\n", text)
        text = re.sub(r"[ \t]{2,}", " ", text)

        return text.strip()
