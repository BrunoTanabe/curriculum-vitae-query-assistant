from django.db import models
from django.utils.translation import gettext_lazy as _

"""
The Enum allowed_images.py.
O enum allowed_images.py define os tipos de imagens permitidos para upload no sistema.

@Author Bruno Tanabe
@CreatedAt 2025-05-08
"""


class AllowedImages(models.TextChoices):
    """
    Enumeração de tipos de imagens permitidos.
    """

    JPG = "jpg", _("JPG")
    JPEG = "jpeg", _("JPEG")
    PNG = "png", _("PNG")
