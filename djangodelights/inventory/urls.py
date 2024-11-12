from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name="home"),
   path('ingredients/', views.IngredientsList.as_view(), name='ingredientslist'),
   path('menuitem/', views.MenusList.as_view(), name="menuslist"),
   path('purchases/', views.purchases, name="purchases"),
   path('reports/', views.reports, name="reports"),
   path('receiperequirements/', views.receiperequirements, name="receiperequirements"),
]