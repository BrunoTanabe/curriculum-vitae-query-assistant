from django.db import models
from django.utils.translation import gettext_lazy as _

"""
The Enum ocr_models.py.
O enum ocr_models.py define quais são os modelos de OCR disponíveis no sistema.  

@Author Bruno Tanabe
@CreatedAt 2025-05-10
"""


class OCRModels(models.TextChoices):
    """
    Enumeração para os modelos de LLM disponíveis.

    Esta classe define os possíveis modelos de LLM que podem ser utilizados no sistema.
    Ela utiliza as TextChoices do Django para fornecer um conjunto de opções predefinidas para um campo de modelo.

    EASYOCR (str): Representa o modelo Easy OCR.
    """

    EASYOCR = "easy_ocr", _("Easy OCR")
