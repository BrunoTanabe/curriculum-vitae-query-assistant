import easyocr
import numpy as np
from PIL import Image, ImageOps

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

    # TODO: adicionar configurção e passo a passo para habilitar a GPU
    def __init__(self, languages: list[str] = ["pt", "en"]):
        """
        Inicializa o serviço EasyOCR com os idiomas especificados.
        """
        self.reader = easyocr.Reader(
            lang_list=languages,
            gpu=True,
        )

    def _preprocess_image(self, image_file) -> np.ndarray:
        image_file.seek(0)
        img = Image.open(image_file).convert("RGB")
        gray = ImageOps.grayscale(img)
        return np.array(gray)

    def recognize_text(self, image) -> str:
        try:
            img_np = self._preprocess_image(image)
            model_response = self.reader.readtext(
                image=img_np,
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
            return " ".join([line[1] for line in model_response])
        except Exception as e:
            raise ReadTextException(detail=image.name)
