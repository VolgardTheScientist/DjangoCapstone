from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name="home"),
   path('ingredients/', views.IngredientsList.as_view(), name='ingredientslist'),
   path('menuitem/', views.MenusList.as_view(), name="menuslist"),
   path('purchases/', views.PurchasesList.as_view(), name="purchaseslist"),
   path('reports/', views.reports, name="reports"),
   path('receipes/', views.ReceipesList.as_view(), name="receiperequirements"),
   path("ingredients/delete/<pk>", views.IngredientDelete.as_view(), name="ingredientdelete"),
   path("menuitem/create", views.AddMenuItemCreate.as_view(), name="menuitemcreate"),
   path("ingredient/create", views.AddIngredientCreate.as_view(), name="ingredientcreate"),
   path("receipe/create", views.AddReceipeCreate.as_view(), name="receipecreate"),
   path("purchase/create", views.AddPurchaseCreate.as_view(), name="purchasecreate"),
]