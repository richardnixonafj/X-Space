from django.http import HttpResponse
from spacex.base import lancamentos

get_next_launch = lancamentos.get_next_launch()

def home(request):
    return HttpResponse(get_next_launch)
