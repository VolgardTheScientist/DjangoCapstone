from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name="home"),
   path('ingredients/', views.ingredients, name="ingredients"),
   path('menuitem/', views.menus, name="menus"),
   path('purchases/', views.purchases, name="purchases"),
   path('reports/', views.reports, name="reports"),
   path('receiperequirements/', views.receiperequirements, name="receiperequirements"),
]