from django.http import HttpResponse
from spacex.base import lancamentos


def home(request):
    return HttpResponse('Desafio Zapay')

def proxlanc(request):
    return HttpResponse(lancamentos.get_proximo_lancamento())

def ultlanc(request):
    return HttpResponse(lancamentos.get_ultimo_lancamento())

def proxslancs(request):
    return HttpResponse(lancamentos.get_proximos_lancamentos())

def lancspas(request):
    return HttpResponse(lancamentos.get_lancamentos_passados())
