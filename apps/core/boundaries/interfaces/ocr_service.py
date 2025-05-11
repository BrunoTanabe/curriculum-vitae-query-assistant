from abc import ABC, abstractmethod

"""
The Service ocr_service.py.
O service ocr_service.py é responsável por fornecer uma interface para serviços de reconhecimento óptico de caracteres (OCR).

@Author Bruno Tanabe
@CreatedAt 2025-05-10
"""


class OCRService(ABC):
    """
    Classe os serviços de reconhecimento óptico de caracteres (OCR).
    Esta classe define a interface para serviços de OCR, permitindo realizar reconhecimento óptico de caracteres em imagens.
    """

    @abstractmethod
    def __init__(self, languages: list[str] = ["pt", "en"]):
        """
        Inicializa o serviço OCR com os idiomas especificados.
        """
        self.languages = languages

    @abstractmethod
    def __prepare_image(self, image):
        """
        Prepara a imagem para o reconhecimento óptico de caracteres (OCR).
        """
        pass

    @abstractmethod
    def recognize_text(self, image) -> str:
        """
        Realiza o reconhecimento óptico de caracteres (OCR) em uma lista de imagens.
        """
        pass
