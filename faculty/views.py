from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    return HttpResponse("Hello, world. You're at the faculty home.")
