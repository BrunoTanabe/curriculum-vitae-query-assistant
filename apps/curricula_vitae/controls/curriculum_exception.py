from rest_framework import status

from apps.core.controls.custom_api_exception import CustomAPIException

"""
The Script curriculum_exception.py.
O arquivo curriculum_exception.py contém exceções personalizadas para o módulo de currículos.

@Author Bruno Tanabe
@CreatedAt 2025-05-08
"""


class PostCurriculumException(CustomAPIException):
    """
    Exceção para erros não mapeados ao criar um currículo.
    """

    def __init__(self):

        error = {
            "error": "Não foi possível enviar os dados referentes aos currículos, tente novamente mais tarde."
        }
        code = status.HTTP_500_INTERNAL_SERVER_ERROR

        super().__init__(error=error, code=code)
