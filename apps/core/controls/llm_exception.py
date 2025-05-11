from rest_framework import status

from apps.core.controls.custom_api_exception import CustomAPIException

"""
The Script llm_exception.py.
O arquivo llm_exception.py contém exceções personalizadas para o módulo de LLM (Modelos de Linguagem Grande).

@Author Bruno Tanabe
@CreatedAt 2025-05-10
"""


class CurriculumAnalysis(CustomAPIException):
    """
    Exceção para erro ao processar a resposta da análise de currículos.
    """

    def __init__(self):
        error = {
            "error": "Não foi possível obter a resposta da análise de currículos. Tente novamente mais tarde."
        }
        code = status.HTTP_500_INTERNAL_SERVER_ERROR

        super().__init__(error=error, code=code)


class CurriculumSummarization(CustomAPIException):
    """
    Exceção para erro ao processar a resposta do resumo de currículos.
    """

    def __init__(self):
        error = {
            "error": "Não foi possível obter a resposta do resumo de currículos. Tente novamente mais tarde."
        }
        code = status.HTTP_500_INTERNAL_SERVER_ERROR

        super().__init__(error=error, code=code)
