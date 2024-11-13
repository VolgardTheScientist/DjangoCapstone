from django.shortcuts import render
from django.views.generic import ListView, DeleteView
from .models import Ingredient, MenuItem, ReceipeRequirement, Purchase
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import AddMenuItem, AddIngredient, AddReceipe, AddPurchase

def home(request):
  return render(request, "inventory/home.html")

# def ingredients(request):
#   return render(request, "inventory/ingredients.html")

# def menus(request):
#   return render(request, "inventory/menuitem.html")

# def purchases(request):
#   return render(request, "inventory/purchases.html")

def reports(request):
  return render(request, "inventory/reports.html")

def receiperequirements(request):
  return render(request, "inventory/receipes.html")

class IngredientsList(ListView):
  model = Ingredient
  template_name = "inventory/ingredients.html"

class MenusList(ListView):
  model = MenuItem
  template_name = "inventory/menus.html"

class IngredientDelete(DeleteView):
  model = Ingredient
  template_name = "inventory/ingredient_delete_form.html"
  success_url = reverse_lazy('ingredientslist')

class PurchasesList(ListView):
  model = Purchase
  template_name = "inventory/purchases.html"

class ReceipesList(ListView):
  model = ReceipeRequirement
  template_name = "inventory/receipes.html"

class AddMenuItemCreate(CreateView):
  model = MenuItem
  template_name = "inventory/add_menu_item.html"
  form_class = AddMenuItem

class AddIngredientCreate(CreateView):
  model = Ingredient
  template_name = "inventory/add_menu_item.html"
  form_class = AddIngredient

class AddReceipeCreate(CreateView):
  model = ReceipeRequirement
  template_name = "inventory/add_receipe.html"
  form_class = AddReceipe

class AddPurchaseCreate(CreateView):
  model = Purchase
  template_name = "inventory/add_purchase.html"
  form_class = AddPurchase
  success_url = reverse_lazy('purchaseslist')
