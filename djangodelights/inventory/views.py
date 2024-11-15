from django.shortcuts import render
from django.views.generic import ListView, DeleteView
from .models import Ingredient, MenuItem, ReceipeRequirement, Purchase
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from .forms import AddMenuItem, AddIngredient, AddReceipe, AddPurchase, IngredientUpdateForm

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

class IngredientUpdate(UpdateView):
  model = Ingredient
  template_name = "inventory/ingredient_update_form.html"
  form_class = IngredientUpdateForm
  success_url = reverse_lazy('ingredientslist')

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

def sales_report(request):
    purchases = Purchase.objects.all()

    total_revenue = 0
    total_profit = 0

    sales_data = []
    for purchase in purchases:
        item = purchase.menu_item
        cost = purchase.calculate_cost()
        revenue = purchase.calculate_revenue()
        profit = purchase.calculate_profit()

        sales_data.append({
            'title': item.title,
            'cost': cost,
            'price': item.price,
            'profit': profit,
        })

        total_revenue += revenue
        total_profit += profit

    return render(request, 'inventory/sales_report.html', {
        'sales_data': sales_data,
        'total_revenue': total_revenue,
        'total_profit': total_profit
    })
