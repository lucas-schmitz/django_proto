from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    return HttpResponse("This is the homepage! and Arthur is a jackass")