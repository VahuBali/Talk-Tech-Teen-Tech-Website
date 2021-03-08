from django.shortcuts import render
from .models import product

# Create your views here.


def index(request):
    return render(request, 'index.html')


def listen(request):
    return render(request, 'listen.html')


def prem(request):
    return render(request, 'prem.html')


def func_djgscofa():

    return


def prodospecs(request):

    prods = product.objects.all()

    return render(request, 'prodospecs.html', {'products': prods})


def contact(request):
    return render(request, 'contact.html')


def signup(request):
    return render(request, 'signup.html')
