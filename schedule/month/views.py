from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def January(request):
    return HttpResponse('This is January')

def February(request):
    return HttpResponse('This is Fabruary')

def March(request):
    return HttpResponse('This is March')

def April(request):
    return HttpResponse('This is April')

def May(request):
    return HttpResponse('This is May')    