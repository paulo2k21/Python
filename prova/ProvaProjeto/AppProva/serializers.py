from rest_framework import serializers
from .models import Reclamacao, Produto, Usuario, Nivel
from rest_framework import serializers

class ReclamacaoSerializers (serializers.ModelSerializer):

    class Meta:
        model = Reclamacao
        fields = ["id", "inicio", "fim", "produto", "usuario", "nivel"]


