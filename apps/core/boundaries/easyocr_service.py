import easyocr

from apps.core.boundaries.interfaces.ocr_service import OCRService
from apps.core.controls.ocr_exception import ReadTextException

"""
The Service easyocr_service.py.
O service easyocr_service.py é responsável por fornecer uma interface para o EasyOCR, uma biblioteca de reconhecimento óptico de caracteres (OCR) que suporta múltiplos idiomas e scripts.
Ele encapsula a lógica de inicialização do EasyOCR e fornece métodos para realizar OCR em imagens, retornando os resultados em um formato estruturado.

@Author Bruno Tanabe
@CreatedAt 2025-05-10
"""


class EasyOCRService(OCRService):
    """
    Classe de serviço para EasyOCR.
    Esta classe encapsula a funcionalidade do EasyOCR, permitindo realizar reconhecimento óptico de caracteres (OCR) em imagens.
    """

    def __init__(self, languages: list[str] = ["pt", "en"]):
        """
        Inicializa o serviço EasyOCR com os idiomas especificados.
        """
        self.reader = easyocr.Reader(
            lang_list=languages,
            gpu=True,
        )

    # TODO: IMPLEMENTAR TRATAMENTO DE IMAGENS
    def prepare_image(self, image):
        """
        Prepara a imagem para o reconhecimento óptico de caracteres (OCR).
        """
        # Aqui você pode adicionar qualquer pré-processamento necessário na imagem
        return image

    def recognize_text(self, image) -> str:
        """
        Realiza o reconhecimento óptico de caracteres (OCR) em uma lista de imagens.
        """

        result = ""

        try:
            image = self.__prepare_image(image)

            model_response = self.reader.readtext(
                image=image,
                batch_size=8,
                paragraph=True,
                blocklist=["$"],
                width_ths=0.8,
                add_margin=0.2,
                x_ths=0.9,
                y_ths=0.6,
                min_size=20,
                link_threshold=0.2,
            )

            for line in model_response:
                result += line[1]
                result += "\n"

            return result

        except Exception:
            raise ReadTextException(detail=image.name)
