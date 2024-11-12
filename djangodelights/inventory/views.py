from django.shortcuts import render
from django.views.generic import ListView
from .models import Ingredient, MenuItem, ReceipeRequirement, Purchase

def home(request):
  return render(request, "inventory/home.html")

# def ingredients(request):
#   return render(request, "inventory/ingredients.html")

# def menus(request):
#   return render(request, "inventory/menuitem.html")

def purchases(request):
  return render(request, "inventory/purchases.html")

def reports(request):
  return render(request, "inventory/reports.html")

def receiperequirements(request):
  return render(request, "inventory/receiperequirements.html")

class IngredientsList(ListView):
  model = Ingredient
  template_name = "inventory/ingredients.html"

class MenusList(ListView):
  model = MenuItem
  template_name = "inventory/menus.html"