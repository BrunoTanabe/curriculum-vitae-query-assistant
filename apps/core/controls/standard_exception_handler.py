from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler

from apps.core.controls.standard_api_response import \
    StandardApiResponse

"""
The Method custom_api_exception.py.
O método custom_api_exception.py é um manipulador de exceções personalizado para o projeto, ele padroniza as respostas de erro da API.

@Author Bruno Tanabe
@CreatedAt 2025-05-07
"""


def standard_exception_handler(exc, context):
    """
    Manipulador de exceções personalizado para padronizar as respostas de erro.
    """

    try:
        response = exception_handler(exc, context)

        request = context.get("request")
        path = request.path if request else None
        method = request.method if request else None

        if response is None:
            # TODO: Adicionar mais exceções específicas
            if isinstance(exc, Http404):
                status_code = status.HTTP_404_NOT_FOUND
                error_data = {"detail": "Recurso não encontrado."}
            else:
                status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
                error_data = {"detail": "Ocorreu um erro interno no servidor."}
        else:
            status_code = response.status_code
            error_data = response.data

        api_response = StandardApiResponse.error(
            error_data=error_data, code=status_code, path=path, method=method
        )

        return Response(api_response.to_dict(), status=status_code)
    except Exception:
        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        error_data = {"detail": "Ocorreu um erro interno no servidor."}

        api_response = StandardApiResponse.error(
            error_data=error_data, code=status_code, path=None, method=None
        )

        return Response(api_response.to_dict(), status=status_code)
