from django.http import JsonResponse
from .models import RecipeCategory
from .models import Recipe
from .models import RecipeIngredients
from .models import Instruction


def get_category_recipes(request):
    categories = RecipeCategory.objects.all()
    

    responseData = []
    for category in categories:
        responseData.append({
            'name': category.name,
            'urlImg': category.urlImg,
        })
    return JsonResponse(responseData, safe=False)

 
def get_recipes_by_id(request):
    recipeId = request.GET.get('recipeId')

    if recipeId is None:
        recipes = None
    else:
        recipes = Recipe.objects.filter(pk=recipeId)

    responseData = {}
    arrayIngredients = []
    arraySteps = []

    for recipe in recipes:
        ingredients = RecipeIngredients.objects.filter(recipe__pk=recipe.id)
        
        for ingr in ingredients:
            arrayIngredients.append({
                'name': ingr.ingredient.name,
                'quantity': ingr.quantity,
        })

        steps = recipe.steps.all()
        for step in steps:
            arrayIngredientsByStep = []
            ingredientsUsed = step.ingredientsUsed.all()
            for ingrUsed in ingredientsUsed:
                arrayIngredientsByStep.append({
                    'name': ingrUsed.name,
                    'quantity': "ingrUsed.urlImg",
                })

            arraySteps.append({
                'stepIndex': step.stepIndex,
                'name': step.name,
                'description': step.description,
                'urlImg': step.urlImg,
                'urlVideo': step.urlVideo,
                'ingredientsUsed': arrayIngredientsByStep
        })
        
        responseData = {
            'name': recipe.name,
            'duration': recipe.duration,
            'description': recipe.description,
            'urlTeaserVideo': recipe.urlTeaserVideo,
            'servings': recipe.servings,
            'steps': arraySteps,
            'ingredients': arrayIngredients
        }
    return JsonResponse(responseData)



def get_recipes_from_category(request):
    categoryRequest = request.GET.get('category')

    if categoryRequest is None:
        recipes = Recipe.objects.all()
    else:
        recipes = Recipe.objects.filter(category__name=categoryRequest)

    responseData = []
   
    for recipe in recipes:
        
        responseData.append({
            'id': recipe.pk,
            'name': recipe.name,
            'duration': recipe.duration,
            'urlThumb': recipe.urlImg,
            'isVegan': recipe.isVegan
        })
    return JsonResponse(responseData, safe=False)
