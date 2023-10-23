from django.contrib import admin
from cbi_recipe_appplication.models import Recipe
from cbi_recipe_appplication.models import Instruction
from cbi_recipe_appplication.models import Ingredient
from cbi_recipe_appplication.models import RecipeCategory
from cbi_recipe_appplication.models import RecipeIngredients

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Instruction)
admin.site.register(Ingredient)
admin.site.register(RecipeCategory)
admin.site.register(RecipeIngredients)