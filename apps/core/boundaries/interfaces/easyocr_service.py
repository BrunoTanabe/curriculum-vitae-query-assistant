import easyocr

"""
The Service easyocr_service.py.
O service easyocr_service.py é responsável por fornecer uma interface para o EasyOCR, uma biblioteca de reconhecimento óptico de caracteres (OCR) que suporta múltiplos idiomas e scripts.
Ele encapsula a lógica de inicialização do EasyOCR e fornece métodos para realizar OCR em imagens, retornando os resultados em um formato estruturado.

@Author Bruno Tanabe
@CreatedAt 2025-05-10
"""

class EasyOCRService:
    """
    Classe de serviço para EasyOCR.
    Esta classe encapsula a funcionalidade do EasyOCR, permitindo realizar reconhecimento óptico de caracteres (OCR) em imagens.
    """

    def __init__(self, languages: list[str] = ["pt"]):
        """
        Inicializa o serviço EasyOCR com os idiomas especificados.
        """
        self.reader = easyocr.Reader(
            lang_list=languages,
            gpu=False,
        )

    def __del__(self):
        """
        Destrói o serviço EasyOCR.
        """
        del self.reader

    def prepare_image(self, image):
        """
        Prepara a imagem para o reconhecimento óptico de caracteres (OCR).
        """
        # Aqui você pode adicionar qualquer pré-processamento necessário na imagem
        return image

    def recognize_text(self, image):
        """
        Realiza o reconhecimento óptico de caracteres (OCR) em uma lista de imagens.
        """
        results = self.reader.readtext(image)
        return [
            {
                "text": result[1],
                "confidence": result[2],
                "bounding_box": result[0],
            }
            for result in results
        ]

    def recognize_text_list(self, images: list):
        """
        Realiza o reconhecimento óptico de caracteres (OCR) em uma lista de imagens.
        """

        results = ""

        """
        das as orientações de texto possíveis.
        """

        for image in images:
            image = self.prepare_image(image)
            results += f"CURRÍCULO {images.index(image)}\n"
            results += self.reader.readtext(
                # configurações gerais
                image=image,
                batch_size=4,
                # paragraph=True,
                rotation_info=[90, 180, 270]
            )
            results += "\n\n"
