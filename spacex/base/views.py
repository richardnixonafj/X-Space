from django.http import HttpResponse
from spacex.base import lancamentos


def home(request):
    return HttpResponse(lancamentos.get_ultimo_lancamento())
