from django.shortcuts import render
from django.http import HTTPResponse
# Create your views here.
def index(request):
    return HTTPResponse("Hello world. You're at the polls index")