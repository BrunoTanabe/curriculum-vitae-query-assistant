from dependency_injector.wiring import Provide, inject
from rest_framework import status
from rest_framework.views import APIView

from apps.core.controls.custom_api_exception import CustomAPIException
from apps.core.controls.standard_response_mixin import StandardResponseMixin
from apps.curricula_vitae.containers.curriculum_container import \
    CurriculumContainer
from apps.curricula_vitae.controls.curriculum_exception import \
    PostCurriculumException
from apps.curricula_vitae.entities.serializers.curriculum_create_input import \
    CurriculumCreateInput

"""
The View curriculum_api_view.py.
A view curriculum_api_view.py é responsável por lidar com as requisições HTTP relacionadas aos documentos.

@Author Bruno Tanabe
@CreatedAt 2025-05-07
"""


class CurriculumAPIView(StandardResponseMixin, APIView):

    @inject
    @document_post
    def post(
        self,
        request,
        identification_document_service: IdDocumentService = Provide[
            CurriculumContainer.identification_document_service
        ],
    ):
        """
        Método para criar um documento de identificação.
        """

        try:
            serializer = CurriculumCreateInput(data=request.data)
            if not serializer.is_valid():
                return self.get_error_response(
                    error_data=serializer.errors, status_code=status.HTTP_400_BAD_REQUEST
                )

            validated = serializer.validated_data

            document = identification_document_service.create(
                name=validated.get("name"),
                document_type=validated.get("type"),
                file=validated["file"],
            )
            output_serializer = CurriculumCreateOutput(document)

            return self.get_success_response(
                output_serializer.data, status.HTTP_201_CREATED
            )
        except CustomAPIException as e:
            return self.get_error_response(
                error_data={"detail": str(e.detail)},
                status_code=e.status_code,
            )
        except Exception:
            return self.get_error_response(PostCurriculumException())
