from rest_framework import status
from rest_framework.renderers import JSONRenderer

from apps.core.controls.standard_api_response import StandardApiResponse

"""
The Renderer standard_response_renderer.py.
O renderer standard_response_renderer.py é um renderer personalizado para o projeto que renderiza as respostas da API em um formato padronizado.

@Author Bruno Tanabe
@CreatedAt 2025-05-07
"""


class StandardResponseRenderer(JSONRenderer):
    """
    Renderer customizado para padronizar todas as respostas da API.
    Transforma o conteúdo em um formato padronizado antes de serializá-lo para JSON.
    """

    def render(self, data, accepted_media_type=None, renderer_context=None):
        """
        Renderiza a resposta no formato padronizado.
        """
        if renderer_context is None:
            renderer_context = {}

        request = renderer_context.get("request")
        response = renderer_context.get("response")

        if request:
            path = request.path
            method = request.method
        else:
            path = None
            method = None

        if isinstance(data, dict) and all(
            key in data for key in ["code", "status", "response", "path", "method"]
        ):
            standardized_data = data
        else:
            if response and response.status_code >= 400:
                api_response = StandardApiResponse.error(
                    error_data=data,
                    code=response.status_code or status.HTTP_400_BAD_REQUEST,
                    path=path,
                    method=method,
                )
            else:
                api_response = StandardApiResponse.success(
                    data=data,
                    code=response.status_code or status.HTTP_200_OK,
                    path=path,
                    method=method,
                )

            standardized_data = api_response.to_dict()

        return super().render(standardized_data, accepted_media_type, renderer_context)
