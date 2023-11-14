from django.shortcuts import render
from django.http import HttpResponse


def hello_world(request):
    return HttpResponse('hello world')


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def service(request):
    return render(request, 'service.html')


def contact(request):
    return render(request, 'contact.html')