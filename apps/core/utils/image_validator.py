from PIL import Image
from django.core.exceptions import ValidationError
from django.core.validators import validate_image_file_extension
from django.utils.translation import gettext_lazy as _

"""
The Validator image_validator.py.
O validador image_validator.py é responsável por validar arquivos de imagem, garantindo que eles estejam no formato correto e não estejam corrompidos.
    
    @Author Bruno Tanabe
    @CreatedAt 2025-05-07
"""

ALLOWED_IMAGE_FORMATS = ["JPEG", "JPG", "PNG"]


def image_validator(file):
    try:
        validate_image_file_extension(file)

        image = Image.open(file)
        image_format = image.format
        if image_format not in ALLOWED_IMAGE_FORMATS:
            raise ValidationError(
                _(
                    f"O campo 'file' está corrompido ou não é uma imagem válida. Os tipos permitidos são: {', '.join(ALLOWED_IMAGE_FORMATS)}."
                )
            )
    except ValidationError:
        raise ValidationError(
            _(
                f"O campo 'file' está corrompido ou não é uma imagem válida. Os tipos permitidos são: {', '.join(ALLOWED_IMAGE_FORMATS)}."
            )
        )
    except Exception:
        raise ValidationError(
            _(
                f"O campo 'file' está corrompido ou não é uma imagem válida. Os tipos permitidos são: {', '.join(ALLOWED_IMAGE_FORMATS)}."
            )
        )
