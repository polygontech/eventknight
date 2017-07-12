from django.shortcuts import render
from django.http import HttpResponse
from .ek_engine import ek_send


# Create your views here.
def fire_up_ek_engine(request):
    ek_send()
    return HttpResponse("EK_Engine : started")
