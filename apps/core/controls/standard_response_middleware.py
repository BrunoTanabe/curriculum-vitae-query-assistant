import json

from django.http import JsonResponse

from apps.core.controls.standard_api_response import StandardApiResponse

"""
The Middleware standard_response_middleware.py.
O middleware standard_response_middleware.py é um middleware que vai padronizar as respostas HTTP.

@Author Bruno Tanabe
@CreatedAt 2025-05-07
"""


# TODO: Melhorar a implementação do middleware, lógica pode ser simplificada
class StandardResponseMiddleware:
    """
    Middleware para padronizar respostas HTTP de erro que não são processadas pelo DRF.
    Garante que mesmo erros gerados pelo Django core sejam formatados no padrão da API.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)

        if 400 <= response.status_code < 600:
            content_type = response.get("Content-Type", "")

            # formata o json se ele não estiver formatado
            if "application/json" in content_type:
                try:
                    response_data = json.loads(response.content)

                    if not (
                        isinstance(response_data, dict)
                        and all(
                            key in response_data
                            for key in ["code", "status", "response", "path", "method"]
                        )
                    ):
                        api_response = StandardApiResponse.error(
                            error_data=response_data,
                            code=response.status_code,
                            path=request.path,
                            method=request.method,
                        )

                        return JsonResponse(
                            api_response.to_dict(), status=response.status_code
                        )
                except json.JSONDecodeError:
                    error_data = {"detail": "Erro de formato de resposta"}

                    api_response = StandardApiResponse.error(
                        error_data=error_data,
                        code=response.status_code,
                        path=request.path,
                        method=request.method,
                    )

                    return JsonResponse(api_response.to_dict(), status=response.status_code)

        return response
