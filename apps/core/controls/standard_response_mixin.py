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

    def get_success_response(self, data=None, status_code=status.HTTP_200_OK):
        """
        Cria uma resposta de sucesso padronizada.
        """
        request = self.request
        api_response = StandardApiResponse.success(
            data=data, code=status_code, path=request.path, method=request.method
        )
        return Response(api_response.to_dict(), status=status_code)

    def get_error_response(self, error_data=None, status_code=status.HTTP_400_BAD_REQUEST):
        """
        Cria uma resposta de erro padronizada.

        Aceita um dicionário `error_data` ou uma instância de `CustomAPIException`.
        """
        request = self.request

        if isinstance(error_data, CustomAPIException):
            status_code = error_data.status_code
            error_data = error_data.detail
        else:
            error_data = {
                "error": error_data if error_data else "Ocorrreu um erro inesperado.",
            }

        api_response = StandardApiResponse.error(
            error_data=error_data,
            code=status_code,
            path=request.path,
            method=request.method,
        )

        return Response(api_response.to_dict(), status=status_code)
