from django.shortcuts import render
from AppProva.serializers import ReclamacaoSerializers
from AppProva.models import Reclamacao
from rest_framework.response import Response

from rest_framework.decorators import api_view


@api_view(['GET0', 'POST'])
def reclamacao_list(request):
    if request.method == 'GET':
        reclamacao = Reclamacao.objects.all()
        serializer = ReclamacaoSerializer(reclamacoes, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ReclamacaoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# Create your views here.



