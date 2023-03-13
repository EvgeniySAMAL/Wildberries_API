from django.shortcuts import render
from django.http import HttpResponse
import requests


def index(request):
    return HttpResponse('<h1>привет</h1>')

