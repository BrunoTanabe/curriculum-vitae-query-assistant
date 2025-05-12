from django.apps import AppConfig

"""
The Script apps.py.
O arquivo apps.py é responsável por configurar o aplicativo curricula_vitae dentro do projeto Django.

@Author Bruno Tanabe
@CreatedAt 2025-05-07
"""


class DocumentsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.curricula_vitae"

    def ready(self):
        from apps.curricula_vitae.containers.curriculum_container import \
            CurriculumContainer

        container = CurriculumContainer()
        container.wire(modules=["apps.curricula_vitae.boundaries.curriculum_api_view"])
