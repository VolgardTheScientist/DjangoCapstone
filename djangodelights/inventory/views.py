from django.shortcuts import render, redirect
from django.views.generic import ListView, DeleteView
from .models import Ingredient, MenuItem, ReceipeRequirement, Purchase
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from .forms import AddMenuItem, AddIngredient, AddReceipe, AddPurchase, IngredientUpdateForm

#Login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout

def logout_view(request):
  logout(request)
  return redirect("home")

@login_required
def home(request):
  return render(request, "inventory/home.html")

@login_required
def reports(request):
  return render(request, "inventory/reports.html")

@login_required
def receiperequirements(request):
  return render(request, "inventory/receipes.html")

class IngredientsList(LoginRequiredMixin,ListView):
  model = Ingredient
  template_name = "inventory/ingredients.html"

class MenusList(LoginRequiredMixin, ListView):
  model = MenuItem
  template_name = "inventory/menus.html"

class IngredientUpdate(LoginRequiredMixin, UpdateView):
  model = Ingredient
  template_name = "inventory/ingredient_update_form.html"
  form_class = IngredientUpdateForm
  success_url = reverse_lazy('ingredientslist')

class IngredientDelete(LoginRequiredMixin, DeleteView):
  model = Ingredient
  template_name = "inventory/ingredient_delete_form.html"
  success_url = reverse_lazy('ingredientslist')

class PurchasesList(LoginRequiredMixin, ListView):
  model = Purchase
  template_name = "inventory/purchases.html"

class ReceipesList(LoginRequiredMixin, ListView):
  model = ReceipeRequirement
  template_name = "inventory/receipes.html"

class AddMenuItemCreate(LoginRequiredMixin, CreateView):
  model = MenuItem
  template_name = "inventory/add_menu_item.html"
  form_class = AddMenuItem

class AddIngredientCreate(LoginRequiredMixin, CreateView):
  model = Ingredient
  template_name = "inventory/add_menu_item.html"
  form_class = AddIngredient

class AddReceipeCreate(LoginRequiredMixin, CreateView):
  model = ReceipeRequirement
  template_name = "inventory/add_receipe.html"
  form_class = AddReceipe

class AddPurchaseCreate(LoginRequiredMixin, CreateView):
  model = Purchase
  template_name = "inventory/add_purchase.html"
  form_class = AddPurchase
  success_url = reverse_lazy('purchaseslist')

@login_required
def sales_report(request):
    purchases = Purchase.objects.all()

    total_revenue = 0
    total_profit = 0
    total_cost = 0

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
        total_cost  += cost

    return render(request, 'inventory/sales_report.html', {
        'sales_data': sales_data,
        'total_cost': total_cost,
        'total_revenue': total_revenue,
        'total_profit': total_profit
    })
