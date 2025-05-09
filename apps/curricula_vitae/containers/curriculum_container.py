from dependency_injector import containers, providers
from django.conf import settings

"""
The Class curriculum_container.py.
A classe curriculum_container.py é um contêiner de injeção de dependência que fornece instâncias de serviços e armazenamento para o aplicativo de curriculos.

@Author Bruno Tanabe
@CreatedAt 2025-05-08
"""


class CurriculumContainer(containers.DeclarativeContainer):
    """
    Container para o serviço de currículos.
    """

    wiring_config = containers.WiringConfiguration(
        modules=["apps.curricula_vitae.boundaries.curriculum_api_view"]
    )

    application_storage = settings.APPLICATION_STORAGE

    if application_storage == "aws":
        aws_storage = providers.Singleton(AWSStorage)
        identification_document_service = providers.Factory(
            CurriculumService, storage=aws_storage
        )
    elif application_storage == "local":
        local_storage = providers.Singleton(LocalStorage)
        identification_document_service = providers.Factory(
            CurriculumService, storage=local_storage
        )
    else:
        raise ValueError(
            f"Tipo de armazenamento inválido: {application_storage}. "
            "Apenas 'aws' ou 'local' são suportados."
        )
