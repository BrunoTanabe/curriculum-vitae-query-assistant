from django.db import models
from django.utils.translation import gettext_lazy as _

"""
The Enum allowed_files.py.
O enum allowed_files.py define os tipos de arquivos permitidos para upload no sistema, inclue PDF, JPG, JPEG e PNG.

@Author Bruno Tanabe
@CreatedAt 2025-05-08
"""


class AllowedFiles(models.TextChoices):
    """
    Enumeração de tipos de arquivos permitidos.
    """

    PDF = "pdf", _("PDF")
    JPG = "jpg", _("JPG")
    JPEG = "jpeg", _("JPEG")
    PNG = "png", _("PNG")
