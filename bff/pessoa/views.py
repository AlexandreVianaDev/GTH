from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Pessoa
from .serializers import PessoaSerializer
from .service import Service


class PessoaView(APIView):
    def post(self, request):
        try:
            serializer = PessoaSerializer(data=request.data)

            if serializer.is_valid():
                dto = serializer.validated_data
                service = Service()
                response = service.save(dto)
                return Response(response, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(f"Erro ao criar Pessoa: {e}")
            return Response(
                {"message": "Erro ao criar Pessoa", "error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def get(self, request):
        try:
            service = Service()
            response = service.get(request)
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            print(f"Erro ao buscar Pessoa: {e}")
            return Response(
                {"message": "Erro ao buscar Pessoa", "error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def calculate_ideal_weight(self, request):
        try:
            serializer = PessoaSerializer(data=request.data)

            if serializer.is_valid():
                dto = serializer.validated_data
                service = Service()
                response = service.calculate_ideal_weight(dto)
                return Response(response, status=status.HTTP_200_OK)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(f"Erro ao calcular peso ideal: {e}")
            return Response(
                {"message": "Erro ao calcular peso ideal", "error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class PessoaDetailView(APIView):
    def put(self, request, id):
        try:
            if not id:
                return Response(
                    {"message": "ID não fornecido"}, status=status.HTTP_400_BAD_REQUEST
                )
            serializer = PessoaSerializer(data=request.data)

            if serializer.is_valid():
                dto = serializer.validated_data
                service = Service()
                response = service.update(dto, id)
                return Response(response, status=status.HTTP_200_OK)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Pessoa.DoesNotExist as e:
            return Response(
                {"message": "Pessoa não encontrada", "error": str(e)},
                status=status.HTTP_404_NOT_FOUND,
            )
        except Exception as e:
            print(f"Erro ao atualizar Pessoa: {e}")
            return Response(
                {"message": "Erro ao atualizar Pessoa", "error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def delete(self, _, id):
        try:
            if not id:
                return Response(
                    {"message": "ID não fornecido"}, status=status.HTTP_400_BAD_REQUEST
                )

            service = Service()
            service.delete(id)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Pessoa.DoesNotExist as e:
            return Response(
                {"message": "Pessoa não encontrada", "error": str(e)},
                status=status.HTTP_404_NOT_FOUND,
            )
        except Exception as e:
            print(f"Erro ao excluir Pessoa: {e}")
            return Response(
                {"message": "Erro ao excluir Pessoa", "error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
