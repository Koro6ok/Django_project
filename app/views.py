import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def status_view(request):
    return HttpResponse("All is OK!")

def random_color(request):
    ran_col = "#" + "".join(random.sample("0123456789abcdef", 6))
    return HttpResponse("Color of this time is " + ran_col)
