from dependency_injector.wiring import Provide, inject
from rest_framework import status
from rest_framework.views import APIView

from apps.core.controls.custom_api_exception import CustomAPIException
from apps.core.controls.standard_response_mixin import StandardResponseMixin
from apps.curricula_vitae.boundaries.curriculum_doc import curriculum_post
from apps.curricula_vitae.boundaries.curriculum_service import \
    CurriculumService
from apps.curricula_vitae.containers.curriculum_container import \
    CurriculumContainer
from apps.curricula_vitae.controls.curriculum_exception import \
    PostCurriculumException
from apps.curricula_vitae.entities.serializers.curriculum_create_input import \
    CurriculumCreateInput
from apps.curricula_vitae.entities.serializers.curriculum_create_output import \
    CurriculumCreateOutput

"""
The View curriculum_api_view.py.
A view curriculum_api_view.py é responsável por lidar com as requisições HTTP relacionadas aos documentos.

@Author Bruno Tanabe
@CreatedAt 2025-05-07
"""


class CurriculumAPIView(StandardResponseMixin, APIView):

    @curriculum_post
    @inject
    def post(
        self,
        request,
        curriculum_service: CurriculumService = Provide[
            CurriculumContainer.curriculum_service
        ],
    ):
        """
        Método para realizar o upload de um ou mais currículos e receber a resposta do LLM.
        """
        try:
            input_serializer = CurriculumCreateInput(data=request.data)

            if not input_serializer.is_valid():
                return self.get_error_response(
                    error=input_serializer.errors, code=status.HTTP_400_BAD_REQUEST
                )

            response = curriculum_service.create(input_serializer.validated_data)
            output_serializer = CurriculumCreateOutput(response)

            return self.get_success_response(
                output_serializer.data,
                status.HTTP_200_OK,
            )
        except CustomAPIException as e:
            return self.get_error_response(
                error={"error": str(e.error)},
                code=e.status_code,
            )
        except Exception as e:
            print(e)
            return self.get_error_response(PostCurriculumException())
