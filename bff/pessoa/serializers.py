from rest_framework import serializers

from pessoa.models import Pessoa


class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = [
            "id",
            "nome",
            "data_nasc",
            "cpf",
            "sexo",
            "altura",
            "peso",
        ]
