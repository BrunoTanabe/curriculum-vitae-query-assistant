from django.conf import settings
from huggingface_hub import InferenceClient

from apps.core.boundaries.interfaces.llm_service import LLMService
from apps.core.controls.llm_exception import (CurriculumAnalysis,
                                              CurriculumSummarization)

"""
The Service huggingface_service.py.
O service huggingface_service.py é responsável por interagir com a API do Hugging Face para utilizar Large Language Models (LLMs) para tarefas de processamento de linguagem natural.
Ele encapsula a lógica de chamada da API, incluindo autenticação e manipulação de respostas, permitindo que outras partes do sistema utilizem modelos LLMs de forma simplificada.

@Author Bruno Tanabe
@CreatedAt 2025-05-10
"""


class HuggingFaceService(LLMService):
    """
    Classe de serviço para interagir com a API do Hugging Face.
    Esta classe encapsula a funcionalidade da API do Hugging Face, permitindo realizar chamadas para modelos LLMs.
    """

    def __init__(self):
        """
        Inicializa o serviço Hugging Face com a chave de autenticação.
        """
        self.client = InferenceClient(
            provider="hf-inference", api_key=settings.HUGGINGFACE_ACCESS_TOKEN
        )

    # TODO: Definir prompt para análise de currículo
    def curriculum_analysis(self, curriculum: str, query) -> str:
        """
        Realiza a análise de um currículo utilizando o modelo LLM do Hugging Face.
        """
        try:
            completion = self.client.chat.completions.create(
                model="deepseek-ai/DeepSeek-V3-0324",
                temperature=1.0,
                response_format="text",
                messages=[{"role": "user", "content": curriculum}],
            )

            return completion.choices[0].message
        except Exception:
            raise CurriculumAnalysis()

    # TODO: Definir prompt para sumarização de currículo
    def curriculum_summarization(self, curriculum: str) -> str:
        """
        Realiza a sumarização de um currículo utilizando o modelo LLM do Hugging Face.
        """
        try:
            completion = self.client.chat.completions.create(
                model="deepseek-ai/DeepSeek-V3-0324",
                temperature=1.0,
                response_format="json",
                messages=[{"role": "user", "content": curriculum}],
            )

            return completion.choices[0].message
        except Exception:
            raise CurriculumSummarization()
