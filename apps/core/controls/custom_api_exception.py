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

    def __init__(self, detail=None, status_code=None):
        if detail is None:
            detail = "Ocorreu um erro inesperado."
        if status_code is None:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

        self.detail = detail
        self.status_code = status_code
