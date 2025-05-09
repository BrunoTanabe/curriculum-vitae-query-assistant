import os

from django.core.exceptions import ValidationError
from django.core.validators import validate_image_file_extension
from django.utils.translation import gettext_lazy as _
from PIL import Image
from PyPDF2 import PdfReader

from apps.core.entities.enums.allowed_files import AllowedFiles
from apps.core.entities.enums.allowed_images import AllowedImages

"""
The Validator file_validator.py.
O validador file_validator.py é responsável por validar os arquivos enviados pelo usuário, garantindo que eles estejam no formato correto e não estejam corrompidos.

@Author Bruno Tanabe
@CreatedAt 2025-05-08
"""


def file_validator(file):
    """
    Valida o arquivo enviado pelo usuário.
    """

    ext = os.path.splitext(file.name)[1].lower().replace(".", "")

    if ext not in AllowedFiles.values():
        raise ValidationError(
            _(
                f"O campo 'files' aceita apenas os seguintes tipos de arquivo: {', '.join(AllowedFiles.values())}."
            )
        )

    if ext in ["jpeg", "jpg", "png"]:
        try:
            validate_image_file_extension(file)

            image = Image.open(file)
            image_format = image.format.upper()

            if image_format not in AllowedImages.values():
                raise ValidationError(
                    _(
                        f"Um ou imagens do campo 'files' é inválido ou está corrompido. Formatos de imagem permitidos: {', '.join(AllowedImages.values())}."
                    )
                )
        except Exception:
            raise ValidationError(
                _(
                    f"Um ou imagens do campo 'files' não pôdem ser abertos como imagem. Formatos permitidos: {', '.join(AllowedImages.values())}."
                )
            )
    elif ext == "pdf":
        try:
            file.seek(0)  # importante para garantir que a leitura comece do início
            PdfReader(file)  # apenas tenta abrir, se falhar é inválido
        except Exception:
            raise ValidationError(
                _(f"Um ou mais PDFs do campo 'files' estão corrompidos ou inválidos..")
            )
    else:
        raise ValidationError(
            _(
                f"O campo 'files' aceita apenas os seguintes tipos de arquivo: {', '.join(AllowedFiles.values())}."
            )
        )
