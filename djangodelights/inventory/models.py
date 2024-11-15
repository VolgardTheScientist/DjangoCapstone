from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  
    unit_price = models.IntegerField(default=0)

    GRAM = "g"
    KILOGRAM = "kg"
    LITER = "l"
    MILLILITER = "ml"
    TEASPOON = "tsp"
    TABLESPOON = "tbsp"
    CUP = "cup"
    PIECE = "pc"
    PINCH = "pinch"

    KITCHEN_UNIT_CHOICES = [
        (GRAM, "Gram"),
        (KILOGRAM, "Kilogram"),
        (LITER, "Liter"),
        (MILLILITER, "Milliliter"),
        (TEASPOON, "Teaspoon"),
        (TABLESPOON, "Tablespoon"),
        (CUP, "Cup"),
        (PIECE, "Piece"),
        (PINCH, "Pinch"),
    ]

    unit = models.CharField(max_length=5, choices=KITCHEN_UNIT_CHOICES, default = GRAM)

    def __str__(self):
        return self.name 
    # + ", " + self.quantity + ", " + self.unit+ ", " + self.unit_price

    class Meta:
        ordering = ["name"]

    def get_absolute_url(self):
        return reverse("ingredientcreate") 

class MenuItem(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  

    def __str__(self):
        return self.title 
    class Meta:
        ordering = ["title"]   
    def get_absolute_url(self):
        return reverse("menuitemcreate") 
    
    def calculate_cost(self):
        total_cost = 0
        for req in self.receiperequirement_set.all():
            total_cost += req.quantity * req.ingredient.unit_price
        return total_cost

    def calculate_profit(self):
        cost = self.calculate_cost()
        return self.price - cost


class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Purchase of {self.menu_item} on {self.date.strftime('%Y-%m-%d %H:%M:%S')}"
    
    def calculate_cost(self):
        return self.menu_item.calculate_cost()

    def calculate_revenue(self):
        return self.menu_item.price

    def calculate_profit(self):
        return self.calculate_revenue() - self.calculate_cost()



class ReceipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  

    def __str__(self):
        return f"{self.menu_item} - {self.ingredient} (Qty: {self.quantity})"
    class Meta:
        ordering = ["menu_item"]
    def get_absolute_url(self):
        return reverse("receipecreate") 
    
