from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza
# Create your views here.

def index(request):
    pizza = Pizza.objects.all()
    """pizza_details = []
    for pizza in pizza:
        pizza_details.append(pizza.nom+" : "+str(pizza.print)+" xof")
    return HttpResponse("les pizzas: "+", ".join(pizza_details))"""
    return render(request,'menu/index.html',{'pizza':pizza})