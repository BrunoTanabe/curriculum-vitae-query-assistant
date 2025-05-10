from django.db import models
from django.utils.translation import gettext_lazy as _

"""
The Enum llm_models.py.
O enum llm_models.py define quais são os modelos de LLM (Large Language Model) disponíveis no sistema.

@Author Bruno Tanabe
@CreatedAt 2025-05-10
"""


class LLMModels(models.TextChoices):
    """
    Enumeração para os modelos de LLM disponíveis.

    Esta classe define os possíveis modelos de LLM que podem ser utilizados no sistema.
    Ela utiliza as TextChoices do Django para fornecer um conjunto de opções predefinidas para um campo de modelo.

    LLAMA3 (str): Representa o modelo Llama 3.
    GPT4 (str): Representa o modelo GPT-4.
    GPT4_32K (str): Representa o modelo GPT-4 com 32k tokens.
    GPT3_5 (str): Representa o modelo GPT-3.5.
    """

    LLAMA3 = "llama3", _("Llama 3")
    GPT4 = "gpt4", _("GPT-4")
    GPT4_32K = "gpt4-32k", _("GPT-4 32k")
    GPT3_5 = "gpt3.5", _("GPT-3.5")
