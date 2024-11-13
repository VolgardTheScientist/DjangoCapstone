from django import forms
from .models import Ingredient, MenuItem, ReceipeRequirement, Purchase

class AddMenuItem(forms.ModelForm):
  class Meta:
    model = MenuItem
    fields = ("__all__")

class AddIngredient(forms.ModelForm):
  class Meta:
    model = Ingredient
    fields = ("__all__")

class AddReceipe(forms.ModelForm):
  class Meta:
    model = ReceipeRequirement
    fields = ("__all__")

class AddPurchase(forms.ModelForm):
  class Meta:
    model = Purchase
    fields = ("__all__")