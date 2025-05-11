from abc import ABC, abstractmethod

"""
The Interface pdf_service.py.
O service pdf_service.py é responsável por fornecer uma interface para serviços de manipulação de arquivos PDF.
Ele encapsula a lógica de extração de texto e manipulação de arquivos PDF, permitindo realizar operações como leitura e normalização de texto.

@Author Bruno Tanabe
@CreatedAt 2025-05-11
"""


class PDFService(ABC):
    """
    Classe de serviços de manipulação de arquivos PDF.
    Esta classe define a interface para serviços de PDF, permitindo realizar operações como leitura e normalização de texto.
    """

    @abstractmethod
    def __init__(self):
        """
        Inicializa o serviço PDF.
        """
        pass

    @abstractmethod
    def extract_text(self, file) -> str:
        """
        Extrai o texto de um arquivo PDF.
        """
        pass

    @abstractmethod
    def _normalize_text(self, text: str) -> str:
        """
        Normaliza o texto extraído de um arquivo PDF.
        """
        pass
