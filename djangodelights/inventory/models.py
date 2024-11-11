from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)    
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

# class Menu(models.Model):
#     name = models.CharField(max_length=200)
#     quantity = models.IntegerField(default=0)
#     unit = models.IntegerField(default=0)
#     owner = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
# 
# class Purchase(models.Model):
#   pass
# 
# class Receipe(models.Model):
#   pass