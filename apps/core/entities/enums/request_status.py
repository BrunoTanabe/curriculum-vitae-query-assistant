from django.db import models
from django.utils.translation import gettext_lazy as _

"""
The Enum request_status.py.
O Enum request_status.py enum é uma enumeração que define os possíveis status de uma requisição.

@Author Bruno Tanabe
@CreatedAt 2025-05-10
"""


class RequestStatus(models.TextChoices):
    """
    Enumeração de tipos de imagens permitidos.
    """

    SUCCESS = "SUCCESS", _("Success")
    ERROR = "ERROR", _("Error")
