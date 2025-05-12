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

    LLAMA3_1 (str): Representa o modelo Meta Llama 3.1 8B Instruct.
    """

    LLAMA3_1 = (
        "meta-llama/Llama-3.1-8B-Instruct",
        _("Meta Llama 3.1 8B Instruct"),
    )
