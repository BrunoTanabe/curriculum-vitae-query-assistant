from rest_framework import serializers

from apps.core.entities.enums.allowed_files import AllowedFiles
from apps.core.utils.file_validator import file_validator

"""
The Serializer curriculum_create_input.py.
O serializador curriculum_create_input.py valida e processa os dados de entrada para a criação de um currículo.

@Author Bruno Tanabe
@CreatedAt 2025-05-080
"""


class CurriculumCreateInput(serializers.Serializer):
    """
    Serializer para entrada de dados ao criar um documento de identificação.
    """

    files = serializers.ListField(
        child=serializers.FileField(
            allow_empty_file=False,
            validators=[file_validator],
            help_text=f"Currículo, arquivos permitidos: {', '.join(AllowedFiles.values)}.",
            error_messages={
                "allow_empty_file": "O campo 'files' tem um ou mais arquivos vazios.",
            },
        ),
        required=True,
        allow_empty=False,
        help_text=f"Currículos, arquivos permitidos: {', '.join(AllowedFiles.values)}.",
        error_messages={
            "required": "O campo 'files' é obrigatório.",
            "allow_empty": "O campo 'files' não pode estar vazio.",
            "invalid": "O campo 'files' deve ser uma lista de um ou mais arquivos.",
        },
    )

    query = serializers.CharField(
        allow_blank=False,
        allow_null=False,
        required=False,
        max_length=256,
        default="",
        help_text="Sua pergunta (máx. 256 caracteres). Caso deseje obter uma lista com o resumo do currículo de todos os candidatos, deixe esse campo TOTALMENTE vazio (sem espaços) ou não envie esse campo.",
        error_messages={
            f"max_length": "O campo 'query' deve ter no máximo 256 caracteres.",
            f"blank": "O campo 'query' não pode estar vazio. Se não quiser fazer uma pergunta, deixe o campo vazio (sem espaços) ou não envie esse campo.",
            f"null": "O campo 'query' não pode ser nulo. Se não quiser fazer uma pergunta, deixe o campo vazio (sem espaços) ou não envie esse campo.",
        },
    )

    request_id = serializers.UUIDField(
        allow_null=False,
        required=True,
        help_text="ID da requisição (UUID)",
        error_messages={
            f"blank": "O campo 'request_id' não pode estar vazio.",
            f"null": "O campo 'request_id' não pode ser nulo.",
            f"required": "O campo 'request_id' é obrigatório.",
            f"invalid": "O campo 'request_id' deve ser um UUID válido.",
        },
    )

    user_id = serializers.UUIDField(
        allow_null=False,
        required=True,
        help_text="ID do usuário (UUID)",
        error_messages={
            f"blank": "O campo 'user_id' não pode estar vazio.",
            f"null": "O campo 'user_id' não pode ser nulo.",
            f"required": "O campo 'user_id' é obrigatório.",
            f"invalid": "O campo 'user_id' deve ser um UUID válido.",
        },
    )

    class Meta:
        fields = ["files", "query", "request_id", "user_id"]

    # TODO: determinar o tamanho máximo para os arquivos e dimensões mínimas e máximas para as imagens
