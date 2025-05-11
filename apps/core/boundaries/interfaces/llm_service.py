from abc import ABC, abstractmethod

"""
The Service llm_service.py.
O service llm_service.py é responsável por fornecer uma interface para serviços de linguagem de modelo (LLM).
Ele encapsula a lógica de interação com modelos de linguagem, permitindo realizar tarefas como análise e sumarização de currículos.

@Author Bruno Tanabe
@CreatedAt 2025-05-10
"""


class LLMService(ABC):
    """
    Classe de serviços de linguagem de modelo (LLM).
    Esta classe define a interface para serviços de LLM, permitindo realizar tarefas como análise e sumarização de currículos.
    """

    @abstractmethod
    def __init__(self):
        """
        Inicializa o serviço LLM.
        """
        pass

    @abstractmethod
    def curriculum_analysis(self, curriculum: str, query) -> str:
        """
        Realiza a análise de um currículo utilizando o modelo LLM.
        """
        pass

    @abstractmethod
    def curriculum_summarization(self, curriculum: str) -> str:
        """
        Realiza a sumarização de um currículo utilizando o modelo LLM.
        """
        pass
