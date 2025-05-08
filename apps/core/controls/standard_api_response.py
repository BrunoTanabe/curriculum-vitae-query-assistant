from rest_framework import status

"""
The Class standard_api_response.py.
A classe standard_api_response.py é responsável por padronizar a estrutura das respostas da API.

@Author Bruno Tanabe
@CreatedAt 2025-05-07
"""


class StandardApiResponse:
    """
    Classe responsável por padronizar a estrutura das respostas da API.
    Todas as respostas seguirão o formato definido nesta classe.
    """

    def __init__(self, code=None, status_msg=None, response=None, path=None, method=None):
        self.code = code
        self.status_msg = status_msg
        self.response = response if response is not None else {}
        self.path = path
        self.method = method

    def to_dict(self):
        """
        Converte o objeto de resposta para um dicionário que será serializado em JSON.
        """
        return {
            "code": self.code,
            "status": self.status_msg,
            "response": self.response,
            "path": self.path,
            "method": self.method,
        }

    @classmethod
    def success(cls, data=None, code=status.HTTP_200_OK, path=None, method=None):
        """
        Cria uma resposta de sucesso padronizada.
        """
        return cls(code=code, status_msg="SUCCESS", response=data, path=path, method=method)

    @classmethod
    def error(
            cls, error_data=None, code=status.HTTP_400_BAD_REQUEST, path=None, method=None
    ):
        """
        Cria uma resposta de erro padronizada.
        """
        return cls(
            code=code, status_msg="ERROR", response=error_data, path=path, method=method
        )
