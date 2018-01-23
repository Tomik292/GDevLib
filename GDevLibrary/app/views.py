
from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

def login(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/login.html')

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/main.html')

def main_unity(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
       'app/unity_main.html')

def main_unreal(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/unreal_main.html')

def main_cry(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
       'app/cry_main.html')
