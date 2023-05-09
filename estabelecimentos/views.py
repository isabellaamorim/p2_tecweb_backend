from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .models import Estabelecimento
from .serializers import EstabelecimentoSerializer
from django.http import HttpResponse
import json

# SUAS OUTRAS FUNÇÕES CONTINUAM AQUI

def index(request):
    return HttpResponse("Olá mundo! Este é o app notes de Tecnologias Web do Insper.")

@api_view(['POST', 'GET'])
def favoritar(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data["name"]
        adress = data["adress"]

        Estabelecimento.objects.create(name=name, adress=adress)

    estabelecimentos = Estabelecimento.objects.all()
    serialized_estabelecimento = EstabelecimentoSerializer(estabelecimentos, many=True)
    
    return Response(serialized_estabelecimento.data)
