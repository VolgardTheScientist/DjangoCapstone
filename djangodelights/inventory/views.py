from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
# def home():
#   template = loader.get_template("inventory/home.html")
#   return HttpResponse(template.render())

def home(request):
  return render(request, "inventory/home.html")