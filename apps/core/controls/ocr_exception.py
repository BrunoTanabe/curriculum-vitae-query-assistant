from rest_framework import status

from apps.core.controls.custom_api_exception import CustomAPIException
from apps.core.entities.enums.allowed_images import AllowedImages

"""
The Script ocr_exception.py.
O arquivo ocr_exception.py contém exceções personalizadas para o módulo de OCR (Reconhecimento Óptico de Caracteres).

@Author Bruno Tanabe
@CreatedAt 2025-05-10
"""


class ReadTextException(CustomAPIException):
    """
    Exceção para erro ao extrair texto de uma imagem.
    """

    def __init__(self, detail=None):
        if detail is None:
            error = f"Não foi possível extrair a informação de um ou mais currículos. Verifique se os arquivos {', '.join(AllowedImages.values)} estão legíveis e tente novamente."
            code = status.HTTP_400_BAD_REQUEST
        else:
            error = (
                f"Não foi possível extrair a informação de {detail}. Verifique se o tipo de arquivo é aceito ({', '.join(AllowedImages.values)}), estão legível e tente novamente.",
            )
            code = status.HTTP_400_BAD_REQUEST
        super().__init__(error=error, code=code)
