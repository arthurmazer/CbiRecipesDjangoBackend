from django.db import models

# Create your models here.
class RecipeCategory(models.Model):
    name = models.CharField(max_length=400)
    urlImg = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.name} {self.urlImg}"
        
class Ingredient(models.Model):
    name = models.CharField(max_length=1000)
    urlImg = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.name}"
        
class Instruction(models.Model):
    stepIndex = models.IntegerField()
    name = models.CharField(max_length=400, default="")
    description = models.CharField(max_length=2000)
    urlImg = models.CharField(max_length=1000)
    urlVideo = models.CharField(max_length=1000)
    ingredientsUsed = models.ManyToManyField(Ingredient)

    def __str__(self):
        return f"{self.stepIndex} {self.name} {self.description} {self.urlImg} {self.urlVideo}"
        
        
class Recipe(models.Model):
    duration = models.CharField(max_length=255)
    name = models.CharField(max_length=400)
    description = models.CharField(max_length=2000, default="")
    category = models.ForeignKey(RecipeCategory, on_delete=models.CASCADE, null=True, default=None)
    urlTeaserVideo = models.CharField(max_length=1000, default="")
    urlImg = models.CharField(max_length=1000, default="")
    servings = models.CharField(max_length=255, default="")
    isVegan = models.BooleanField(default=False)
    steps = models.ManyToManyField(Instruction)
    
    def __str__(self):
        return f"{self.name} {self.duration} {self.description} {self.category} {self.urlTeaserVideo} {self.servings} {self.urlImg}"
        
class RecipeIngredients(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.recipe} {self.ingredient} {self.quantity}"        