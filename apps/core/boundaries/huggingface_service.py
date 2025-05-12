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
    def curricula_analysis(self, curricula: str, query: str) -> str:
        """
        Realiza a análise de um currículo utilizando o modelo LLM do Hugging Face.
        """
        try:
            completion = self.client.chat.completions.create(
                model=settings.APPLICATION_LLM_MODEL,
                messages=[
                    {
                        "role": "system",
                        "content": "You are a Talent Acquisition Specialist focused on hiring candidates, primarily in the technology sector. You will be provided with multiple resumes extracted via OCR from images or photos. These texts may contain spelling, formatting, and structural inconsistencies, and the information may appear disorganized. Your task is to logically interpret and organize this content for evaluation purposes, disregarding superficial errors. Each resume will be delimited with '{$$'(start) and '$$}'(end). You will receive a set of resumes followed by one or more questions. Answer each question clearly and concisely in plain text only (no markdown), using a single paragraph. Base your answers strictly on the content provided in the resumes. Do not fabricate or assume information. If the data is insufficient to answer a question, explicitly state that. Always include a final conclusion in your response. If none of the candidates meet the requirements for the position described in the question, it is your responsibility to clearly state that as well. EVERY RESPONSE MUST CONTAIN A FINAL CONCLUSION. DO NOT RETURN ANY EXPLANATIONS OR ADDITIONAL OUTPUT. EVERY RESPONSE IN BRAZILIAN PORTUGUESE.",
                    },
                    {
                        "role": "user",
                        "content": f"De acordo com os currículos abaixo, responda: {query}\n{curricula}.",
                    },
                ],
            )
            return completion.choices[0].message.content
        except Exception as e:
            raise CurriculumAnalysis()

    # TODO: Definir prompt para sumarização de currículo
    def curricula_summarization(self, curricula: str) -> str:
        """
        Realiza a sumarização de um currículo utilizando o modelo LLM do Hugging Face.
        """
        try:

            response_format = {
                "type": "json",
                "value": {
                    "type": "object",
                    "properties": {},
                    "patternProperties": {".*": {"type": "string"}},
                    "additionalProperties": False,
                },
            }

            completion = self.client.chat.completions.create(
                model=settings.APPLICATION_LLM_MODEL,
                # TODO: configurar corretamente o response_format para forçar que a resposta seja um JSON.
                # response_format=response_format,
                messages=[
                    {
                        "role": "system",
                        "content": "You are a Talent Acquisition Specialist focused on recruiting in the technology sector. You will receive raw text extracted from resume images or PDFs using OCR, so expect spelling mistakes, formatting issues, and mixed-up content. These errors should be ignored. Your task is to logically organize and summarize the key information from each resume."
                        "Each resume is marked by `{$$` at the beginning and `$$}` at the end."
                        "Return only **one JSON object** where:"
                        "* Each key is the **candidate's full name** (as best identified from the resume),"
                        "* Each value is a **clear, concise summary** of the candidate's resume,"
                        "* If there is **not enough information** to write a meaningful summary, state that clearly in the summary field, but **do not fabricate or assume** any data."
                        "**Output format:**"
                        "```json"
                        "{"
                        '   "Candidate Name 1": "Summary of resume content."'
                        '   "Candidate Name 2": "Summary of resume content or message that data is insufficient."'
                        "}"
                        "```"
                        "**Important rules:**"
                        "* Always create a summary for each resume, even if the content is minimal."
                        "* Never make up or assume information not clearly supported by the text."
                        "* Only return the final JSON. Do not include explanations or additional output.",
                    },
                    {
                        "role": "user",
                        "content": f"Essa é a lista de currículos, me retorne APENAS o json da resposta: \n{curricula}\n",
                    },
                ],
            )

            return completion.choices[0].message.content
        except Exception as e:
            raise CurriculumSummarization()
