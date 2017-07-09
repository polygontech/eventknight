from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404


def index(request):
    template = 'base/index.html'
    return render(request, template)
