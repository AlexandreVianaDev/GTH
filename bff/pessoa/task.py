import datetime
from .models import Pessoa


class Task:
    def save(self, dto):
        try:
            pessoa = Pessoa(
                id=None,
                pNome=dto["nome"],
                pData=dto["data_nasc"],
                pCPF=dto["cpf"],
                pSexo=dto["sexo"],
                pAltura=dto["altura"],
                pPeso=dto["peso"],
            )
            pessoa.save()
            return {
                "message": "Inclusão realizada com sucesso",
                "pessoa": {
                    "id": pessoa.id,
                    "nome": pessoa.nome,
                    "data_nasc": pessoa.data_nasc,
                    "cpf": pessoa.cpf,
                    "sexo": pessoa.sexo,
                    "altura": pessoa.altura,
                    "peso": pessoa.peso,
                },
            }
        except Exception as e:
            print(f"Erro ao criar Pessoa: {e}")
            raise e

    def update(self, dto, id):
        try:
            pessoa = Pessoa.objects.get(id=id)
            if not pessoa:
                raise Pessoa.DoesNotExist("Pessoa não encontrada")

            pessoa.nome = dto["nome"]
            pessoa.data_nasc = dto["data_nasc"]
            pessoa.cpf = dto["cpf"]
            pessoa.sexo = dto["sexo"]
            pessoa.altura = dto["altura"]
            pessoa.peso = dto["peso"]
            pessoa.save()
            return {
                "message": "Atualização realizada com sucesso",
                "pessoa": {
                    "id": pessoa.id,
                    "nome": pessoa.nome,
                    "data_nasc": pessoa.data_nasc,
                    "cpf": pessoa.cpf,
                    "sexo": pessoa.sexo,
                    "altura": pessoa.altura,
                    "peso": pessoa.peso,
                },
            }
        except (Exception, Pessoa.DoesNotExist) as e:
            print(f"Erro ao atualizar Pessoa: {e}")
            raise e

    def delete(self, id):
        try:
            pessoa = Pessoa.objects.get(id=id)
            if not pessoa:
                raise Pessoa.DoesNotExist("Pessoa não encontrada")

            pessoa.delete()
            return {"message": "Exclusão realizada com sucesso"}
        except (Exception, Pessoa.DoesNotExist) as e:
            print(f"Erro ao excluir Pessoa: {e}")
            raise e

    def get(self, request):
        try:
            pessoas = Pessoa.objects

            id = request.query_params.get("id")
            nome = request.query_params.get("nome")
            data_nasc = request.query_params.get("data_nasc")
            cpf = request.query_params.get("cpf")
            sexo = request.query_params.get("sexo")
            altura = request.query_params.get("altura")
            peso = request.query_params.get("peso")

            if id:
                pessoas = pessoas.filter(id=id)
            if nome:
                pessoas = pessoas.filter(nome__icontains=nome)
            if data_nasc:
                pessoas = pessoas.filter(data_nasc=data_nasc)
            if cpf:
                pessoas = pessoas.filter(cpf=cpf)
            if sexo:
                pessoas = pessoas.filter(sexo=sexo)
            if altura:
                pessoas = pessoas.filter(altura=altura)
            if peso:
                pessoas = pessoas.filter(peso=peso)

            pessoas = pessoas.all()

            return {
                "message": "Consulta realizada com sucesso",
                "pessoas": [
                    {
                        "id": pessoa.id,
                        "nome": pessoa.nome,
                        "data_nasc": (
                            pessoa.data_nasc.strftime("%Y-%m-%d")
                            if isinstance(
                                pessoa.data_nasc, (datetime.date, datetime.datetime)
                            )
                            else pessoa.data_nasc
                        ),
                        "cpf": pessoa.cpf,
                        "sexo": pessoa.sexo,
                        "altura": pessoa.altura,
                        "peso": pessoa.peso,
                    }
                    for pessoa in pessoas
                ],
            }
        except Exception as e:
            print(f"Erro ao consultar Pessoa: {e}")
            raise e

    def search(self, dto: Pessoa):
        try:
            pessoas = Pessoa.objects.all()
            if "nome" in dto:
                pessoas = pessoas.filter(nome__icontains=dto["nome"])
            if "data_nasc" in dto:
                pessoas = pessoas.filter(data_nasc=dto["data_nasc"])
            if "cpf" in dto:
                pessoas = pessoas.filter(cpf=dto["cpf"])
            if "sexo" in dto:
                pessoas = pessoas.filter(sexo=dto["sexo"])
            if "altura" in dto:
                pessoas = pessoas.filter(altura=dto["altura"])
            if "peso" in dto:
                pessoas = pessoas.filter(peso=dto["peso"])

            return {
                "message": "Consulta realizada com sucesso",
                "pessoa": [
                    {
                        "id": pessoa.id,
                        "nome": pessoa.nome,
                        "data_nasc": (
                            pessoa.data_nasc.strftime("%Y-%m-%d")
                            if isinstance(
                                pessoa.data_nasc, (datetime.date, datetime.datetime)
                            )
                            else pessoa.data_nasc
                        ),
                        "cpf": pessoa.cpf,
                        "sexo": pessoa.sexo,
                        "altura": pessoa.altura,
                        "peso": pessoa.peso,
                    }
                    for pessoa in pessoas
                ],
            }
        except Exception as e:
            print(f"Erro ao consultar Pessoa: {e}")
            raise e

    def calculate_ideal_weight(self, dto):
        try:
            pessoa = Pessoa.objects.get(id=dto["id"])
            if not pessoa:
                raise Pessoa.DoesNotExist()
            return {
                "message": "Cálculo realizado com sucesso",
                "peso_ideal": pessoa.CalcularPesoIdeal(),
            }
        except Pessoa.DoesNotExist as e:
            raise Exception("Pessoa não encontrada")
        except Exception as e:
            print(f"Erro ao calcular peso ideal: {e}")
            return e
