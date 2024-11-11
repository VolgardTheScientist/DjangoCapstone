from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def home(request):
  return render(request, "inventory/home.html")

def ingredients(request):
  return render(request, "inventory/ingredients.html")

def menus(request):
  return render(request, "inventory/menuitem.html")

def purchases(request):
  return render(request, "inventory/purchases.html")

def reports(request):
  return render(request, "inventory/reports.html")