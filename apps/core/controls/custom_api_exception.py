from rest_framework import status
from rest_framework.exceptions import APIException

"""
The Class custom_api_exception.py.
A classe custom_api_exception.py define uma exceção personalizada para a API.

@Author Bruno Tanabe
@CreatedAt 2025-05-07
"""


class CustomAPIException(APIException):
    """
    Exceção personalizada base para todas as exceções da API.
    Permite criar exceções com códigos e mensagens específicas.
    """

    def __init__(self, error=None, code=None):
        if error is None:
            error = "Ocorreu um erro inesperado."
        if code is None:
            code = status.HTTP_500_INTERNAL_SERVER_ERROR

        self.error = error
        self.code = code
