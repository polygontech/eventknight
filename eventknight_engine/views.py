from django.shortcuts import render
from django.http import HttpResponse
from .ek_engine import fire_up


# Create your views here.
def fire_up_ek_engine(request):
    fire_up()
    return HttpResponse("EK_Engine : started")
