from rest_framework import status
from rest_framework.response import Response

from apps.core.controls.custom_api_exception import CustomAPIException
from apps.core.controls.standard_api_response import StandardApiResponse

"""
The Class standard_response_mixin.py.
A classe standard_response_mixin.py vai ser usada como interface para as views padronizarem suas respostas.

@Author Bruno Tanabe
@CreatedAt 2025-05-07
"""


class StandardResponseMixin:
    """
    Mixin para ser utilizado nas views que precisam retornar respostas padronizadas.
    """

    def get_success_response(self, data=None, code=status.HTTP_200_OK):
        """
        Cria uma resposta de sucesso padronizada.
        """
        request = self.request
        api_response = StandardApiResponse.success(
            data=data, code=code, path=request.path, method=request.method
        )
        return Response(api_response.to_dict(), status=code)

    def get_error_response(
            self, error="Ocorrreu um erro inesperado.", code=status.HTTP_400_BAD_REQUEST
    ):
        """
        Cria uma resposta de erro padronizada.
        """
        request = self.request

        if isinstance(error, CustomAPIException):
            code = error.code
            error = error.error

        api_response = StandardApiResponse.error(
            error=error,
            code=code,
            path=request.path,
            method=request.method,
        )

        return Response(api_response.to_dict(), status=code)

